import cv2
#import streamlit as st
from ultralytics import solutions

cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
# Placeholder para exibir os frames
#frame_placeholder = st.empty()
# Define region points
line_points = [(20, 400), (1080, 400)]

# Init Object Counter
counter = solutions.ObjectCounter(
    show=False,
    region=line_points,
    model="yolov8n.pt",
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    im0 = counter.count(im0)

      # Converter o frame de BGR (OpenCV) para RGB (para exibir no Streamlit)
    #frame = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)

    # Atualizar o frame no Streamlit
    #frame_placeholder.image(frame, channels="RGB")
    print(counter.names)
    # Pegar a contagem de classes, como pessoas detectadas saindo
    pegaClasse = counter.classwise_counts
    person_out = pegaClasse.get('person', {}).get('OUT', 0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

cap.release()
cv2.destroyAllWindows()
