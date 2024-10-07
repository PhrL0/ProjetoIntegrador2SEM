import cv2
import streamlit as st
from ultralytics import YOLO, solutions

model = YOLO("yolov8s.pt")
cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
frame_placeholder = st.empty()
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

    im0 = counter.count(im0)

    frame_placeholder.image(im0,channels="RGB")
    
    pegaClasse = counter.classwise_counts
    print(pegaClasse)
    person_out = pegaClasse.get('person', {}).get('OUT', 0)
    print(person_out)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()