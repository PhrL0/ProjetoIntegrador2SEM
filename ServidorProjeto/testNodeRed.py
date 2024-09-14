import websocket
import json

url = 'ws://127.0.0.1:1880/ws/data'

# Dados que você quer enviar
data = {
    'ValorA': 30,
    'ValorB': 20,
}

# Função para enviar dados
def on_open(ws):
    ws.send(json.dumps(data))
    ws.close()

# Conectar ao WebSocket
ws = websocket.WebSocketApp(url, on_open=on_open)
ws.run_forever()


