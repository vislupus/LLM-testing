@echo off
setlocal

cd /d "%~dp0"

"C:\Users\n.bojinov\AppData\Local\Programs\Git\bin\bash.exe" -lc "./make_csv.sh README.md scores_by_model.csv scores_by_model_table.md"

pause
