from path_yolo import yolo_segmentation_realsense_once
import cv2
import numpy as np

def pixel_to_robot(all_paths, width=640, height=480, x_max=200, y_max=200):
    robot_paths = []
    for path in all_paths:
        robot_path = []
        for x, y in path:
            x = float(x)
            y = float(y)
            x_robot = (x - width/2) / (width/2) * x_max
            y_robot = (y - height/2) / (height/2) * y_max
            robot_path.append((x_robot, y_robot))
        robot_paths.append(robot_path)
    return robot_paths


