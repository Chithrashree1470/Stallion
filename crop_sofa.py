from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train-4/weights/best.pt")

results = model("test_images/test.jpg", conf=0.01)

img = cv2.imread("test_images/test.jpg")

for r in results:

    boxes = r.boxes.xyxy.cpu().numpy()
    confs = r.boxes.conf.cpu().numpy()

    if len(boxes) > 0:

        best_index = confs.argmax()

        x1, y1, x2, y2 = map(int, boxes[best_index])

        cropped = img[y1:y2, x1:x2]

        cv2.imwrite("best_sofa.jpg", cropped)

print("Best Sofa Cropped Successfully!")