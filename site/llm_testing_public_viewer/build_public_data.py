#!/usr/bin/env python3
"""Build benchmark-data.js from README.md and optional scores.json.

Usage:
    python build_public_data.py
    python build_public_data.py --readme ../README.md --scores ../scores.json --output benchmark-data.js
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TEST_FOLDERS = {
    "02": "02 - Excel clone",
    "12": "12 - 3D castle scene",
    "15": "15 - Space battle simulation",
    "32": "32 - SVG pagoda with dragon",
    "33": "33 - SVG infographic",
    "36": "36 - Voxel world",
}


def clean_cell(value: str) -> str:
    value = re.sub(r"<br\s*/?>", " ", value, flags=re.I)
    value = value.replace("**", "").replace("`", "").replace(r"\|", "|")
    return re.sub(r"\s+", " ", value).strip()


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("М", "M").replace("м", "m")
    return re.sub(r"\s+", " ", value).strip()


def slug(value: str) -> str:
    value = normalize_name(value).lower()
    return re.sub(r"^_+|_+$", "", re.sub(r"[^a-z0-9]+", "_", value))


def parse_readme(markdown: str) -> tuple[list[dict[str, Any]], dict[str, dict[str, float]]]:
    heading_re = re.compile(r"^\s*###\s+(.+?)\s*$", re.M)
    matches = list(heading_re.finditer(markdown.lstrip("\ufeff")))
    tests: list[dict[str, Any]] = []
    readme_scores: dict[str, dict[str, float]] = {}

    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        number_match = re.match(r"^(\d+)", heading)
        if not number_match:
            continue
        number = f"{int(number_match.group(1)):02d}"
        if number not in TEST_FOLDERS:
            continue

        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        body = markdown[start:end]
        table_match = re.search(r"^\s*\|\s*Model\s*\|", body, flags=re.I | re.M)
        prompt_area = body[: table_match.start()] if table_match else body
        prompt = re.sub(r"^\s*---+\s*$", "", prompt_area, flags=re.M)
        prompt = prompt.replace("**", "").strip()

        test_id = f"t{number}"
        title_text = re.sub(r"^\d+\s*-\s*", "", heading).strip()
        tests.append(
            {
                "id": test_id,
                "number": number,
                "title": title_text,
                "displayTitle": f"{number} · {title_text}",
                "folder": TEST_FOLDERS[number],
                "prompt": prompt,
            }
        )

        for line in body.splitlines():
            if not re.match(r"^\s*\|", line):
                continue
            cells = [clean_cell(c) for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            model_name = normalize_name(cells[0])
            score_match = re.search(r"(-?\d+(?:[.,]\d+)?)\s*/\s*10", cells[1], flags=re.I)
            if not score_match or model_name.lower() == "model" or re.fullmatch(r"-+", model_name):
                continue
            score = max(0.0, min(10.0, float(score_match.group(1).replace(",", "."))))
            readme_scores.setdefault(model_name, {})[test_id] = score

    tests.sort(key=lambda t: int(t["number"]))
    if not tests:
        raise ValueError("No benchmark sections were found in README.md")
    return tests, readme_scores


def load_ai_scores(path: Path | None) -> tuple[dict[str, dict[str, dict[str, float]]], list[str]]:
    if not path or not path.exists():
        return {}, []
    raw = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, dict[str, dict[str, float]]] = {}
    judges: set[str] = set()
    for test_id, model_map in raw.items():
        if not isinstance(model_map, dict):
            continue
        for model_id, judge_map in model_map.items():
            if not isinstance(judge_map, dict):
                continue
            for judge_id, entry in judge_map.items():
                if judge_id == "me" or not isinstance(entry, dict):
                    continue
                score = entry.get("overall")
                if isinstance(score, (int, float)):
                    result.setdefault(test_id, {}).setdefault(model_id, {})[judge_id] = float(score)
                    judges.add(judge_id)
    return result, sorted(judges)


def build_data(readme: Path, scores: Path | None) -> dict[str, Any]:
    tests, readme_scores = parse_readme(readme.read_text(encoding="utf-8"))
    ai_scores, judges = load_ai_scores(scores)

    models: list[dict[str, Any]] = []
    for name, per_test in readme_scores.items():
        model_id = slug(name)
        scores_obj: dict[str, Any] = {}
        for test in tests:
            test_id = test["id"]
            readme_score = per_test.get(test_id)
            ai = ai_scores.get(test_id, {}).get(model_id, {})
            scores_obj[test_id] = {"published": readme_score, "ai": ai}
        models.append({"id": model_id, "name": name, "scores": scores_obj})

    # Include models that exist only in scores.json.
    known = {model["id"] for model in models}
    for test_id, model_map in ai_scores.items():
        for model_id in model_map:
            if model_id in known:
                continue
            scores_obj = {
                test["id"]: {
                    "published": None,
                    "ai": ai_scores.get(test["id"], {}).get(model_id, {}),
                }
                for test in tests
            }
            models.append({"id": model_id, "name": model_id.replace("_", " ").title(), "scores": scores_obj})
            known.add(model_id)

    models.sort(key=lambda m: m["name"].lower())
    return {
        "meta": {
            "title": "LLM Testing",
            "subtitle": "Visual benchmark for AI-generated software and creative artifacts",
            "source": readme.name,
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "scoreScale": 10,
        },
        "tests": tests,
        "models": models,
        "judges": judges,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--scores", type=Path, default=Path("scores.json"))
    parser.add_argument("--output", type=Path, default=Path("benchmark-data.js"))
    args = parser.parse_args()

    scores_path = args.scores if args.scores.exists() else None
    data = build_data(args.readme, scores_path)
    payload = "window.BENCHMARK_DATA = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n"
    args.output.write_text(payload, encoding="utf-8")
    print(f"Created {args.output} with {len(data['models'])} models and {len(data['tests'])} tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
