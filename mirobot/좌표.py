import cv2
import wlkatapython
import serial
import time

img = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

coords = []
for cnt in contours:
    for point in cnt:
        x, y = point[0]
        coords.append((int(x), int(y)))

path = []
for (x, y) in coords:
    path.append((x, y, 200, 0, 0, 0))

print(path)


