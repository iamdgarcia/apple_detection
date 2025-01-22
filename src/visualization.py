import cv2

def visualize_detections(image_path, detections, output_path,r=25,c=(241, 7, 200)):
    """Visualize detections by drawing bounding boxes and saving the image."""
    image = cv2.imread(image_path)
    for detection in detections:
        x, y = map(int, detection["center"])
        cv2.circle(image, (x, y), radius=r, color=c, thickness=-1)
    cv2.imwrite(output_path, image)