import cv2
import numpy as np
from ultralytics import YOLO
import pyrealsense2 as rs

def yolo_segmentation_realsense(model_path="yolov8n-seg.pt", conf=0.1, epsilon=2.0):
    model = YOLO(model_path)

    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    pipeline.start(config)

    try:
        print("YOLO Segmentation 시작")

        while True:
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()

            if not color_frame:
                continue

            color_image = np.asanyarray(color_frame.get_data())
            results = model(color_image, conf=conf)

            
            edge_image = np.zeros_like(color_image)
            all_paths = []

        
            if results[0].masks is not None:
                masks = results[0].masks.data.cpu().numpy()

                for mask in masks:
                    mask = (mask * 255).astype(np.uint8)
                    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

                    for cnt in contours:
                        approx = cv2.approxPolyDP(cnt, epsilon, False)
                        path = []

                        for point in approx:
                            x, y = point[0]
                            path.append((x,y))
                            cv2.circle(edge_image, (x, y), 2, (0, 0, 255), -1)

                        all_paths.append(path)


            #cv2.imshow("YOLO Edge-like Output", edge_image)


            ##for i, path in enumerate(all_paths):
                ##print(f"객체 {i+1} 좌표 개수: {len(path)}")

            # ESC 키로 종료
            if cv2.waitKey(1) == 27:
                break

    finally:
        pipeline.stop()
        cv2.destroyAllWindows()

    return all_paths
