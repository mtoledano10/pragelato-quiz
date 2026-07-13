@echo off
cd /d "%~dp0"
set PATH=%PATH%;C:\Program Files\nodejs

if not exist "node_modules" (
  echo Installation des dependances, patientez...
  call npm install
)

for /f "delims=" %%i in ('powershell -NoProfile -Command "(Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notmatch 'Loopback' -and $_.IPAddress -notmatch '^169\.'}).IPAddress | Select-Object -First 1"') do set LOCALIP=%%i

echo.
echo Demarrage de l'application Pragelato ^& Turin...
echo Sur cet ordinateur : http://localhost:3000
echo Depuis un telephone connecte au meme wifi : http://%LOCALIP%:3000
echo (fermez cette fenetre pour arreter l'application)
echo.
node server.js
pause
