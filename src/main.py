from detection import detect_apples
from visualization import visualize_detections
from utils import save_results
import os

INPUT_DIR = "images/input/"
OUTPUT_DIR = "images/output/"
MODEL_PATH = "models/yolo11x.pt"

if __name__ == "__main__":
    for image_name in os.listdir(INPUT_DIR):
        input_path = os.path.join(INPUT_DIR, image_name)
        results = detect_apples(input_path, MODEL_PATH, conf=0.3, iou=0.7)

        output_path = os.path.join(OUTPUT_DIR, f"detected_{image_name}")
        visualize_detections(input_path, results, output_path)
        save_results(results, OUTPUT_DIR,f"detected_{image_name}")