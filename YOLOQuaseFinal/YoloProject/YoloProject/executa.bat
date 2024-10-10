
@echo off

REM Primeiro, execute o script Python com Streamlit
start cmd /k "streamlit run testeYOLOV11.py"

REM Aguarde alguns segundos para garantir que o Streamlit iniciou
timeout /t 5 /nobreak

REM Agora, abra uma nova janela no Google Chrome para a URL do Streamlit
@echo off
start chrome --new-window --start-fullscreen "www.google.com"
