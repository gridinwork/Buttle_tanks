@echo off
cd /d "%~dp0"
where python >nul 2>nul || (echo Python not found. Install Python 3.11+ & pause & exit /b 1)
python -m pip install -r requirements.txt
start "Tank Battle API" python api_server.py
timeout /t 2 >nul
start "Tank Battle Bot" python ai_bot.py
python game.py
