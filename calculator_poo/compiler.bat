@echo off
title compiler

IF EXIST "main.py" (

	echo compaling program...
	python -m pip install pyinstaller
	pyinstaller --onefile --icon=./app.ico --add-data "./calculator_icon.png;." -w main.py
	cls
	echo finish...

) ELSE (
	echo You must have a main.py file to compile.
)

echo Press to continue...
pause>nul
