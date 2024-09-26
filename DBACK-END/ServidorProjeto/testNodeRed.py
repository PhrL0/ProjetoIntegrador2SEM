import websocket
import json
import threading
import time
import random

url = 'ws://127.0.0.1:1880/ws/data'
cont = 1
# Dados que você quer enviar (dinâmicos)
def gerar_dados():
    return {
        'Contador1': cont,
        'Objeto': "Sapato"
    }

# Função para enviar dados
def on_open(ws):
    data = gerar_dados()  # Gera novos dados a cada conexão
    ws.send(json.dumps(data))
    print("Dados enviados com sucesso:", data)
    ws.close()

# Função para conectar ao WebSocket
def conecta_websocket():
    ws = websocket.WebSocketApp(url, on_open=on_open)
    ws.run_forever()

# Função para repetir a conexão periodicamente
def repetir_conexao():
    conecta_websocket()
    # Re-agendar a próxima execução em 1 segundo
    threading.Timer(1.0, repetir_conexao).start()

# Iniciar a tarefa periódica
repetir_conexao()
