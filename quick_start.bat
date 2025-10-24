@echo off
echo ========================================
echo Crypto Bubbles Desktop - Quick Start
echo ========================================
echo.
echo Choose an option:
echo.
echo 1. Run from source (requires Python)
echo 2. Run executable (dist\CryptoBubbles.exe)
echo 3. Build new executable
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto run_source
if "%choice%"=="2" goto run_exe
if "%choice%"=="3" goto build
if "%choice%"=="4" goto end

:run_source
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting application...
python crypto_bubbles_app.py
goto end

:run_exe
echo.
echo Starting executable...
start dist\CryptoBubbles.exe
goto end

:build
echo.
echo Building executable...
python build_exe.py
goto end

:end
echo.
pause
