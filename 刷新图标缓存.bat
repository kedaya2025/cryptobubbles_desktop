@echo off
echo ========================================
echo 刷新 Windows 图标缓存
echo ========================================
echo.
echo 正在清理图标缓存...
echo.

REM 结束 Windows 资源管理器进程
taskkill /f /im explorer.exe

REM 删除图标缓存文件
cd /d %userprofile%\AppData\Local
attrib -h IconCache.db
del IconCache.db /a

REM 删除 Windows 10/11 的图标缓存
cd /d %userprofile%\AppData\Local\Microsoft\Windows\Explorer
del iconcache*.db /a /f

echo.
echo 图标缓存已清理完成！
echo 正在重启资源管理器...
echo.

REM 重启 Windows 资源管理器
start explorer.exe

echo.
echo ========================================
echo 完成！请检查 CryptoBubbles.exe 的图标
echo ========================================
echo.
pause
