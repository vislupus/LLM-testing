#!/usr/bin/env python3
"""Рекурсивно създава PNG изображения от SVG и HTML файлове.

SVG:
- рендерира се с Chromium чрез Playwright;
- при проблем може да използва CairoSVG като fallback.

HTML:
- отваря се като реална страница в Chrome/Edge/Chromium;
- изчаква зададеното време (по подразбиране 20 секунди);
- прави screenshot на видимия viewport.

По подразбиране файлът се пропуска, ако PNG със същото име вече съществува.
Използвай --overwrite само когато искаш повторно създаване.

Примери:
    python svg_to_png.py .
    python svg_to_png.py "15 - Space battle simulation" --wait 20
    python svg_to_png.py . --html-only --wait 20
    python svg_to_png.py . --svg-only
    python svg_to_png.py . --overwrite
"""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import struct
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class SvgSize:
    width: float
    height: float


_LENGTH_RE = re.compile(
    r"^\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)\s*([a-zA-Z%]*)\s*$"
)
_UNIT_TO_PX = {
    "": 1.0,
    "px": 1.0,
    "pt": 96.0 / 72.0,
    "pc": 16.0,
    "in": 96.0,
    "cm": 96.0 / 2.54,
    "mm": 96.0 / 25.4,
    "q": 96.0 / 101.6,
}


def parse_length(value: Optional[str]) -> Optional[float]:
    if not value:
        return None
    match = _LENGTH_RE.match(value)
    if not match:
        return None
    unit = match.group(2).lower()
    if unit == "%" or unit not in _UNIT_TO_PX:
        return None
    return float(match.group(1)) * _UNIT_TO_PX[unit]


def read_svg_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "utf-16", "windows-1251"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def strip_xml_headers(svg_text: str) -> str:
    svg_text = re.sub(
        r"^\s*<\?xml[^>]*\?>", "", svg_text, count=1, flags=re.IGNORECASE
    )
    svg_text = re.sub(
        r"<!DOCTYPE[\s\S]*?>", "", svg_text, count=1, flags=re.IGNORECASE
    )
    return svg_text.strip()


def detect_svg_size(svg_text: str) -> SvgSize:
    try:
        root = ET.fromstring(svg_text)
    except ET.ParseError as exc:
        raise ValueError(f"невалиден SVG/XML: {exc}") from exc

    width = parse_length(root.attrib.get("width"))
    height = parse_length(root.attrib.get("height"))

    view_box = root.attrib.get("viewBox") or root.attrib.get("viewbox")
    vb_width = vb_height = None
    if view_box:
        parts = re.split(r"[\s,]+", view_box.strip())
        if len(parts) == 4:
            try:
                vb_width = abs(float(parts[2]))
                vb_height = abs(float(parts[3]))
            except ValueError:
                pass

    if width and height:
        return SvgSize(width, height)

    if vb_width and vb_height:
        if width and not height:
            height = width * vb_height / vb_width
        elif height and not width:
            width = height * vb_width / vb_height
        else:
            width, height = vb_width, vb_height

    width = width or 1200.0
    height = height or 1200.0
    if width <= 0 or height <= 0:
        raise ValueError("SVG има невалидни размери")
    return SvgSize(width, height)


def target_dimensions(size: SvgSize, scale: float, max_side: int) -> tuple[int, int]:
    width = max(1.0, size.width * scale)
    height = max(1.0, size.height * scale)

    if max_side > 0 and max(width, height) > max_side:
        factor = max_side / max(width, height)
        width *= factor
        height *= factor

    return max(1, round(width)), max(1, round(height))


def discover_browser(explicit: Optional[str] = None) -> Optional[Path]:
    if explicit:
        path = Path(explicit).expanduser()
        if path.is_file():
            return path.resolve()
        found = shutil.which(explicit)
        return Path(found).resolve() if found else None

    for command in (
        "chromium",
        "chromium-browser",
        "google-chrome",
        "google-chrome-stable",
        "chrome",
        "msedge",
        "microsoft-edge",
    ):
        found = shutil.which(command)
        if found:
            return Path(found).resolve()

    candidates: list[Path] = []
    for base in (
        os.environ.get("PROGRAMFILES"),
        os.environ.get("PROGRAMFILES(X86)"),
        os.environ.get("LOCALAPPDATA"),
    ):
        if not base:
            continue
        candidates.extend(
            [
                Path(base) / "Google/Chrome/Application/chrome.exe",
                Path(base) / "Microsoft/Edge/Application/msedge.exe",
                Path(base) / "Chromium/Application/chrome.exe",
            ]
        )

    candidates.extend(
        [
            Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
            Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
            Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
        ]
    )
    return next((path.resolve() for path in candidates if path.is_file()), None)


def make_svg_render_html(
    svg_path: Path,
    svg_text: str,
    width: int,
    height: int,
    background: str,
) -> str:
    base_uri = svg_path.parent.resolve().as_uri() + "/"
    css_background = (
        "transparent" if background.lower() == "transparent" else background
    )

    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<base href="{html.escape(base_uri, quote=True)}">
<style>
html, body {{
  margin: 0;
  padding: 0;
  width: {width}px;
  height: {height}px;
  overflow: hidden;
  background: {css_background};
}}
#stage {{
  width: {width}px;
  height: {height}px;
  overflow: hidden;
  background: {css_background};
}}
#stage > svg {{
  display: block !important;
  width: {width}px !important;
  height: {height}px !important;
  max-width: none !important;
  max-height: none !important;
}}
</style>
</head>
<body>
<div id="stage">{strip_xml_headers(svg_text)}</div>
</body>
</html>
"""


def png_dimensions(path: Path) -> Optional[tuple[int, int]]:
    try:
        header = path.read_bytes()[:24]
        if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
            return None
        return struct.unpack(">II", header[16:24])
    except OSError:
        return None


def launch_browser(playwright, browser_path: Optional[Path]):
    launch_args: list[str] = [
        "--autoplay-policy=no-user-gesture-required",
        "--disable-background-timer-throttling",
        "--disable-renderer-backgrounding",
    ]
    if hasattr(os, "geteuid") and os.geteuid() == 0:
        launch_args.append("--no-sandbox")

    launch_kwargs = {"headless": True, "args": launch_args}
    if browser_path:
        launch_kwargs["executable_path"] = str(browser_path)
    return playwright.chromium.launch(**launch_kwargs)


def render_svg_with_playwright(
    browser_path: Optional[Path],
    svg_path: Path,
    svg_text: str,
    output_path: Path,
    width: int,
    height: int,
    background: str,
    timeout_seconds: int,
) -> None:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "Playwright не е инсталиран. Изпълни: pip install playwright"
        ) from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    page_html = make_svg_render_html(
        svg_path, svg_text, width, height, background
    )

    with sync_playwright() as playwright:
        browser = launch_browser(playwright, browser_path)
        try:
            context = browser.new_context(
                viewport={"width": width, "height": height},
                device_scale_factor=1,
                java_script_enabled=False,
                service_workers="block",
            )
            page = context.new_page()
            page.set_default_timeout(timeout_seconds * 1000)
            page.set_content(page_html, wait_until="load")
            page.wait_for_timeout(250)
            page.screenshot(
                path=str(output_path.resolve()),
                full_page=False,
                omit_background=background.lower() == "transparent",
            )
            context.close()
        finally:
            browser.close()

    actual = png_dimensions(output_path)
    if actual != (width, height):
        output_path.unlink(missing_ok=True)
        raise RuntimeError(f"PNG размерът е {actual}, очакван е {(width, height)}")


def render_html_with_playwright(
    browser_path: Optional[Path],
    html_path: Path,
    output_path: Path,
    width: int,
    height: int,
    wait_seconds: float,
    timeout_seconds: int,
    full_page: bool,
) -> None:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "Playwright не е инсталиран. Изпълни: pip install playwright"
        ) from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = launch_browser(playwright, browser_path)
        try:
            context = browser.new_context(
                viewport={"width": width, "height": height},
                device_scale_factor=1,
                java_script_enabled=True,
                service_workers="allow",
                ignore_https_errors=True,
            )
            page = context.new_page()
            page.set_default_timeout(timeout_seconds * 1000)

            # file:// запазва относителните локални ресурси и позволява CDN заявки.
            page.goto(html_path.resolve().as_uri(), wait_until="load")
            print(f"    Изчакване 5 секунди за пълно зареждане...")
            page.wait_for_timeout(5_000)

            page.screenshot(
                path=str(output_path.resolve()),
                full_page=full_page,
                animations="allow",
            )
            context.close()
        finally:
            browser.close()

    if not output_path.is_file() or output_path.stat().st_size == 0:
        output_path.unlink(missing_ok=True)
        raise RuntimeError("Screenshot файлът не беше създаден")


def render_svg_with_cairosvg(
    svg_path: Path,
    output_path: Path,
    width: int,
    height: int,
    background: str,
) -> None:
    try:
        import cairosvg  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "CairoSVG не е инсталиран. Изпълни: pip install cairosvg"
        ) from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    options = {
        "url": str(svg_path.resolve()),
        "write_to": str(output_path.resolve()),
        "output_width": width,
        "output_height": height,
    }
    if background.lower() != "transparent":
        options["background_color"] = background
    cairosvg.svg2png(**options)


def output_for(source_path: Path, root: Path, output_dir: Optional[Path]) -> Path:
    if output_dir is None:
        return source_path.with_suffix(".png")
    return (output_dir / source_path.relative_to(root)).with_suffix(".png")


def should_skip(png_path: Path, overwrite: bool) -> bool:
    """Пропуска, ако PNG вече съществува, освен при --overwrite."""
    return png_path.exists() and not overwrite


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Рекурсивно създава PNG от SVG и HTML файлове.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "root", nargs="?", default=".", help="Папка или единичен SVG/HTML файл"
    )
    parser.add_argument("--output-dir", type=Path, help="Отделна изходна папка")
    parser.add_argument("--overwrite", action="store_true", help="Презаписва PNG")
    parser.add_argument("--browser", help="Път или команда за Chrome/Edge/Chromium")
    parser.add_argument("--timeout", type=int, default=60, help="Timeout за файл")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--svg-only", action="store_true", help="Обработва само SVG")
    group.add_argument("--html-only", action="store_true", help="Обработва само HTML")

    parser.add_argument("--scale", type=float, default=1.0, help="SVG мащаб")
    parser.add_argument(
        "--max-side",
        type=int,
        default=4096,
        help="Максимална SVG страна; 0 означава без ограничение",
    )
    parser.add_argument(
        "--background", default="white", help="SVG фон или transparent"
    )
    parser.add_argument(
        "--engine",
        choices=("auto", "playwright", "cairosvg"),
        default="auto",
        help="SVG renderer",
    )

    parser.add_argument(
        "--wait",
        type=float,
        default=5.0,
        help="Запазено за съвместимост; HTML винаги изчаква точно 5 секунди",
    )
    parser.add_argument(
        "--html-width", type=int, default=1440, help="Ширина на HTML viewport"
    )
    parser.add_argument(
        "--html-height", type=int, default=1000, help="Височина на HTML viewport"
    )
    parser.add_argument(
        "--full-page",
        action="store_true",
        help="Снима цялата HTML страница, не само viewport",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.scale <= 0:
        print("Грешка: --scale трябва да е над 0.", file=sys.stderr)
        return 2
    if args.max_side < 0:
        print("Грешка: --max-side не може да е отрицателно.", file=sys.stderr)
        return 2
    if args.wait < 0:
        print("Грешка: --wait не може да е отрицателно.", file=sys.stderr)
        return 2
    if args.html_width <= 0 or args.html_height <= 0:
        print("Грешка: HTML размерите трябва да са над 0.", file=sys.stderr)
        return 2

    input_path = Path(args.root).expanduser().resolve()
    if not input_path.exists():
        print(f"Грешка: няма такъв път: {input_path}", file=sys.stderr)
        return 2

    allowed_suffixes: set[str]
    if args.svg_only:
        allowed_suffixes = {".svg"}
    elif args.html_only:
        allowed_suffixes = {".html", ".htm"}
    else:
        allowed_suffixes = {".svg", ".html", ".htm"}

    if input_path.is_file():
        if input_path.suffix.lower() not in allowed_suffixes:
            print("Грешка: файлът не е от избрания тип.", file=sys.stderr)
            return 2
        root = input_path.parent
        source_files = [input_path]
    else:
        root = input_path
        source_files = sorted(
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.lower() in allowed_suffixes
        )

    if not source_files:
        print(f"Не са намерени подходящи файлове в: {input_path}")
        return 0

    output_dir = args.output_dir.expanduser().resolve() if args.output_dir else None
    browser_path = discover_browser(args.browser)

    if browser_path:
        print(f"Browser: {browser_path}")
    else:
        print("Chrome/Edge не е намерен. Playwright ще опита вградения Chromium.")

    html_count = sum(p.suffix.lower() in {".html", ".htm"} for p in source_files)
    svg_count = sum(p.suffix.lower() == ".svg" for p in source_files)
    print(f"Намерени: {svg_count} SVG и {html_count} HTML файла")

    converted = 0
    skipped = 0
    failed = 0

    for index, source_path in enumerate(source_files, start=1):
        png_path = output_for(source_path, root, output_dir)
        label = (
            str(source_path.relative_to(root))
            if source_path.is_relative_to(root)
            else str(source_path)
        )

        if should_skip(png_path, args.overwrite):
            print(f"[{index}/{len(source_files)}] ↷ {label} — PNG вече съществува")
            skipped += 1
            continue

        try:
            suffix = source_path.suffix.lower()

            if suffix in {".html", ".htm"}:
                render_html_with_playwright(
                    browser_path=browser_path,
                    html_path=source_path,
                    output_path=png_path,
                    width=args.html_width,
                    height=args.html_height,
                    wait_seconds=args.wait,
                    timeout_seconds=args.timeout,
                    full_page=args.full_page,
                )
                renderer = f"HTML/Chromium, изчакване {args.wait:g}s"
                dimensions = png_dimensions(png_path)
                size_text = (
                    f"{dimensions[0]}×{dimensions[1]}"
                    if dimensions
                    else f"{args.html_width}×{args.html_height}"
                )
            else:
                svg_text = read_svg_text(source_path)
                size = detect_svg_size(svg_text)
                width, height = target_dimensions(size, args.scale, args.max_side)
                errors: list[str] = []
                renderer = None

                if args.engine in ("auto", "playwright"):
                    try:
                        render_svg_with_playwright(
                            browser_path=browser_path,
                            svg_path=source_path,
                            svg_text=svg_text,
                            output_path=png_path,
                            width=width,
                            height=height,
                            background=args.background,
                            timeout_seconds=args.timeout,
                        )
                        renderer = "SVG/Playwright"
                    except Exception as exc:
                        errors.append(f"Playwright: {exc}")
                        png_path.unlink(missing_ok=True)
                        if args.engine == "playwright":
                            raise

                if renderer is None and args.engine in ("auto", "cairosvg"):
                    try:
                        render_svg_with_cairosvg(
                            svg_path=source_path,
                            output_path=png_path,
                            width=width,
                            height=height,
                            background=args.background,
                        )
                        renderer = "SVG/CairoSVG"
                    except Exception as exc:
                        errors.append(f"CairoSVG: {exc}")
                        png_path.unlink(missing_ok=True)

                if renderer is None:
                    raise RuntimeError(" | ".join(errors))

                size_text = f"{width}×{height}"

            shown_output = (
                png_path.relative_to(output_dir or root)
                if png_path.is_relative_to(output_dir or root)
                else png_path
            )
            print(
                f"[{index}/{len(source_files)}] ✔ {label} → {shown_output} "
                f"({size_text}, {renderer})"
            )
            converted += 1
        except Exception as exc:
            png_path.unlink(missing_ok=True)
            print(
                f"[{index}/{len(source_files)}] ✖ {label}: {exc}",
                file=sys.stderr,
            )
            failed += 1

    print(
        f"\nГотово: {converted} създадени, "
        f"{skipped} пропуснати, {failed} грешки."
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
