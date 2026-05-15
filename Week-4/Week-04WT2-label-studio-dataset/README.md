# 04WT2 - Label Studio YOLO Dataset

Task: object detection using Label Studio and YOLO format.

Source video: Intel sample video `person-bicycle-car-detection.mp4`.

Classes:
- 0: bicycle
- 1: car
- 2: person

Dataset split created from video frames at 10 FPS:
- Train images: 90
- Validation images: 36
- Test images: 413

This folder contains the YOLO dataset structure and metadata:
- `images/train`, `images/val`, `images/test`
- `labels/train`, `labels/val`
- `data.yaml`
- `train.txt`
- `val.txt`
- `classes.txt`

Train and validation images were labeled manually in Label Studio and exported in YOLO format.
