# Working Code
import cv2
import numpy as np
from util import get_limits

yellow = (0, 255, 255)  # Yellow in BGR colorspace

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerlimit, upperlimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)

    coords = np.where(mask > 0)
    if coords[0].size > 0:  # Check if coords is not empty
        y1, x1 = np.min(coords[0]), np.min(coords[1])  # Top-left corner
        y2, x2 = np.max(coords[0]), np.max(coords[1])  # Bottom-right corner

        if x1 != x2 and y1 != y2:  # Check if a valid bounding box exists
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    else:
        print("No yellow object detected in this frame.")  # Or handle it differently

    cv2.imshow('Yellow Object Detection', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()