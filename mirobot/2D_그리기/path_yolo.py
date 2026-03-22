import cv2
import numpy as np
from ultralytics import YOLO
import pyrealsense2 as rs


def yolo_segmentation_realsense_once(model_path="yolov8n-seg.pt", conf=0.1, epsilon=2.0):
    model = YOLO(model_path)
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    pipeline.start(config)

    try:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            return []

        color_image = np.asanyarray(color_frame.get_data())
        results = model(color_image, conf=conf)

        all_paths = []
        if results[0].masks is not None:
            masks = results[0].masks.data.cpu().numpy()
            for mask in masks:
                mask = (mask*255).astype(np.uint8)
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                for cnt in contours:
                    approx = cv2.approxPolyDP(cnt, epsilon, False)
                    path = []
                    for point in approx:
                        x, y = float(point[0][0]), float(point[0][1])
                        path.append((x,y))
                    all_paths.append(path)
    finally:
        pipeline.stop()
        cv2.destroyAllWindows()

    return all_paths