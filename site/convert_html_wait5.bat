@echo off
setlocal
cd /d "%~dp0"

python -c "import playwright" >nul 2>&1
if errorlevel 1 (
  echo Инсталиране на Playwright...
  python -m pip install playwright
)

echo.
echo HTML файловете ще се отворят и ще се изчакат точно 20 секунди след зареждане.
echo Съществуващите PNG файлове ще бъдат пропуснати.
echo.

python html_svg_to_png.py . 
REM python html_svg_to_png.py . --html-only --overwrite

if errorlevel 1 (
  echo.
  echo Имаше грешки. Провери текста по-горе.
) else (
  echo.
  echo Готово.
)
pause
