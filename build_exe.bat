@echo off
cd /d "%~dp0"
where python >nul 2>nul || (echo Python not found. Install Python 3.11+ & pause & exit /b 1)
python -m pip install -r requirements.txt pyinstaller
pyinstaller --noconfirm --onefile --windowed game.py
pause
