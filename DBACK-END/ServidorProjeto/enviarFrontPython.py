import websocket
import threading

# URL do WebSocket (mesma URL usada no HTML)
url = 'ws://127.0.0.1:1880/ws/data'

# Função chamada ao receber uma mensagem
def on_message(ws, message):
    print("Valor recebido do cliente:", message)

# Função chamada quando a conexão é aberta
def on_open(ws):
    print("Conexão WebSocket aberta")

# Função chamada ao fechar a conexão
def on_close(ws):
    print("Conexão WebSocket fechada")

# Função para iniciar o WebSocket
def start_websocket():
    ws = websocket.WebSocketApp(url,
        on_message=on_message,
        on_open=on_open,
        on_close=on_close)
    ws.run_forever()

# Executar o WebSocket em uma thread separada
thread = threading.Thread(target=start_websocket)
thread.start()

