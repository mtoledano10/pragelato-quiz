@echo off
cd /d "%~dp0"

where streamlit >nul 2>nul
if %errorlevel%==0 (
  streamlit run app.py
  goto :end
)

py -m streamlit run app.py 2>nul
if %errorlevel%==0 goto :end

echo Streamlit n'est pas installe sur cet ordinateur.
echo Installez Python puis lancez : pip install -r requirements.txt
echo Ensuite relancez ce fichier.

:end
pause
