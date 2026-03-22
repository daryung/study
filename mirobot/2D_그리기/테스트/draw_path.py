import cv2
import numpy as np
from yolo_edge import yolo_segmentation_realsense

def draw_paths(image, all_paths, close_contour=True, color=(0, 255, 0), thickness=2):
    for path in all_paths:
        if len(path) < 2:
            continue
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i+1]
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)
        if close_contour and len(path) > 2:
            x1, y1 = path[-1]
            x2, y2 = path[0]
            cv2.line(image, (x1, y1), (x2, y2), color, thickness)
    return image

if __name__ == "__main__":

    all_paths, color_image = yolo_segmentation_realsense() 


    edge_image = np.zeros_like(color_image)

    edge_image = draw_paths(edge_image, all_paths, close_contour=True, color=(0, 255, 0), thickness=2)

    cv2.imshow("YOLO Edge + Paths", edge_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("총 객체 수:", len(all_paths))