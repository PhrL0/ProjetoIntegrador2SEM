
import websocket
import json
import threading


class enviarDados:
    
    def gerar_dados(cont1,cont2,cont3):
        return {
            'Contador1': cont1,
            'Contador2': cont2,
            'Contador3': cont3
        }


    def on_open(ws, data):
        ws.send(json.dumps(data))
        #print("Dados enviados com sucesso:", data)



    def conecta_websocket(dados):
        ws = websocket.WebSocketApp(url, on_open=lambda ws: on_open(ws, dados))
        ws.run_forever()



    def repetir_conexao(dados):
        # Executar a conexão de forma assíncrona
        thread = threading.Thread(target=conecta_websocket, args=(dados,))
        thread.start()