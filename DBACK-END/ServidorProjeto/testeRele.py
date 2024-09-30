import websocket
import json
import threading
import streamlit as st
import pandas as pd
import numpy as np

url = 'ws://127.0.0.1:1880/ws/rele'

# Função para gerar dados
def gerar_dados():
    return {
        'rele': botao
    }

# Função chamada quando a conexão é aberta
def on_open(ws):
    data = gerar_dados()  # Gera os dados
    ws.send(json.dumps(data))  # Envia os dados
    print("Dados enviados com sucesso:", data)
    ws.close()  # Fecha a conexão

# Função para conectar ao WebSocket
def conecta_websocket():
    ws = websocket.WebSocketApp(url, on_open=on_open)
    ws.run_forever()

# Inicia a conexão em uma thread separada
thread = threading.Thread(target=conecta_websocket)
thread.start()



if st.button("Desliga"):
    botao = True 

if st.button("Liga"):
    botao = False