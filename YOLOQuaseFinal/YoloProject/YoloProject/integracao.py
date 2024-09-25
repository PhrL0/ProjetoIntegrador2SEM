import cv2
import websocket
import json
import threading
import time

from ultralytics import YOLO, solutions

url = 'ws://127.0.0.1:1880/ws/data'


# Função para gerar dados de contagem
def gerar_dados(cont):
    return {
        'Contador1': cont,
    }


# Função para enviar dados via WebSocket
def on_open(ws, data):
    ws.send(json.dumps(data))
    #print("Dados enviados com sucesso:", data)
    ws.close()


# Função para conectar ao WebSocket e enviar dados
def conecta_websocket(dados):
    ws = websocket.WebSocketApp(url, on_open=lambda ws: on_open(ws, dados))
    ws.run_forever()


# Função para repetir a conexão periodicamente
def repetir_conexao(dados):
    # Executar a conexão de forma assíncrona
    thread = threading.Thread(target=conecta_websocket, args=(dados,))
    thread.start()


model = YOLO("yolov8s.pt")
cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define region points
region_points = [(20, 400), (625, 404), (625, 360), (20, 360)]

# Video writer
video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init Object Counter
counter = solutions.ObjectCounter(
    view_img=True,
    reg_pts=region_points,
    names=model.names,
    draw_tracks=True,
    line_thickness=2,
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    tracks = model.track(im0, persist=True, show=False)

    im0 = counter.start_counting(im0, tracks)
    contador = counter.out_counts
    dados = gerar_dados(contador)
    # Iniciar a tarefa periódica
    repetir_conexao(dados)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
