import cv2
from ultralytics import YOLO

# Carregar o modelo YOLOv8
model = YOLO("runs/detect/train5/weights/best.pt")

# Abrir a webcam (0 para a webcam padrão)
cap = cv2.VideoCapture(0)

# Loop para capturar frames da webcam
while cap.isOpened():
    # Ler um frame da webcam
    success, frame = cap.read()

    if success:
        # Rodar o rastreamento do YOLOv8 no frame, persistindo entre os frames
        results = model.track(frame, persist=True)
        # Visualizar os resultados no frame
        annotated_frame = results[0].plot()

        objDetectado = results[0].boxes.cls.cpu().numpy()
        print(objDetectado)
        if (objDetectado == 0).any():

            print("Existe um objeto")
        else:
            print("Não há objetos")

        # Exibir o frame anotado
        cv2.imshow("YOLOv8 Tracking - Webcam", annotated_frame)

        # Sair do loop se 'q' for pressionado
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Sair do loop se houver falha ao capturar o frame
        break

# Liberar o objeto de captura de vídeo e fechar as janelas
cap.release()
cv2.destroyAllWindows()
