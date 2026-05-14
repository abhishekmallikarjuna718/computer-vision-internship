from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="short_video.mp4",
    save=True,
    conf=0.25
)

print("Object detection video completed.")
