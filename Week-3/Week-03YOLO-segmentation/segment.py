from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

results = model.predict(
    source="images/train",
    save=True,
    conf=0.25
)

print("All training images segmented successfully.")
