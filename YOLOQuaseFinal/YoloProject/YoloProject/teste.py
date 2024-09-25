import cv2
from ultralytics import YOLO
import numpy as np

# Carregar o modelo YOLOv8
model = YOLO("runs/detect/train5/weights/best.pt")

# Abrir a webcam (0 para a webcam padrão)
cap = cv2.VideoCapture(0)

# Variáveis para contagem de objetos
contador = 0
liberado = False

# Loop para capturar frames da webcam
while cap.isOpened():
    # Ler um frame da webcam
    ret, img = cap.read()

    if ret:
        # Rodar o rastreamento do YOLOv8 no frame, persistindo entre os frames
        results = model.track(img, persist=True)

        # Visualizar os resultados no frame
        annotated_frame = results[0].plot()

        # Pega o array da clase
        objDetectado = results[0].boxes.cls.cpu().numpy()

        img = cv2.resize(annotated_frame, (1100, 720))

        # Converter para escala de cinza
        imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Definir a região de interesse (ROI) para a contagem de pixels
        x, y, w, h = 400, 150, 20, 300

        # Aplicar limiarização adaptativa para detecção de movimento
        imgTh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)

        kernel = np.ones((8, 8), np.uint8)
        imgDil = cv2.dilate(imgTh, kernel, iterations=2)

        # Recortar a região de interesse (ROI) e contar pixels brancos
        recorte = imgDil[y:y + h, x:x + w]
        brancos = cv2.countNonZero(recorte)

        # Lógica de contagem de objetos
        if brancos > 1000 and liberado == True:
            if (objDetectado == 0).any():
                liberado = False
                contador += 1

        elif brancos < 1000:
            liberado = True

        # Desenhar o retângulo em torno da ROI e mostrar a contagem
        color = (0, 255, 0) if liberado else (255, 0, 255)
        cv2.rectangle(annotated_frame, (x, y), (x + w, y + h), color, 4)
        cv2.putText(annotated_frame, str(brancos), (x - 30, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        cv2.rectangle(annotated_frame, (575, 155), (575 + 88, 155 + 85), (255, 255, 255), -1)
        cv2.putText(annotated_frame, str(contador), (x + 100, y), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

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
