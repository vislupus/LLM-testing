@echo off
setlocal

cd /d "%~dp0"

REM "C:\Users\n.bojinov\AppData\Local\Programs\Git\bin\bash.exe" -lc "./make_csv.sh README.md scores_by_model.csv scores_by_model_table.md"
"C:\Users\n.bojinov\Programs\git\bin\bash.exe" -lc "./make_csv.sh README.md scores_by_model.csv scores_by_model_table.md"

pause
