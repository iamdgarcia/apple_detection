from ultralytics import YOLO

def detect_apples(image_path, model_path, conf=0.3, iou=0.7):
    """Detect apples in the given image and return their coordinates."""
    model = YOLO(model_path)
    results = model.predict(source=image_path, conf=conf, iou=iou,verbose=False,classes=[47])#Detecting only 'apple' class

    detections = []
    for r in results[0].boxes.data.cpu().numpy():
        x1, y1, x2, y2, conf, _ = r
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        detections.append({
            "center": (float(x_center), float(y_center)),
            "confidence": float(conf)
        })
    return detections