import cv2
import websocket
import json
import threading
import time

from ultralytics import YOLO, solutions

url = 'ws://127.0.0.1:1880/ws/data'


def gerar_dados(cont):
    return {
        'Contador1': cont,
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

model = YOLO("yolov8s.pt")
cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
listaVerifica = set()
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

    if contador not in listaVerifica:
        listaVerifica.add(contador)
        dados = gerar_dados(contador)
        repetir_conexao(dados)

    for track in tracks:
        if track.boxes is not None:
            for box in track.boxes:
                class_id = int(box.cls)
                print(class_id)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
