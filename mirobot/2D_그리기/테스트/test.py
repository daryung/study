import cv2
import numpy as np

# 검정 이미지 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)

# 선 그리기
cv2.line(img, (100,100), (500,400), (0,255,0), 3)

cv2.imshow("Test Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()