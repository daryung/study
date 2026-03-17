import pyrealsense2 as rs
import cv2
import numpy as np

def main():
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    profile = pipeline.start(config)
    depth_intrinsics = profile.get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()

    try:
        print("카메라 시작")

        while True:
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            depth_frame = frames.get_depth_frame()

            if not color_frame or not depth_frame:
                continue

            color_image = np.asanyarray(color_frame.get_data())
            gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            edges = cv2.Canny(blurred, 100, 200)

            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            robot_path = []

            filtered_contours = []
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > 2000:
                    filtered_contours.append(cnt)

                    approx = cv2.approxPolyDP(cnt, 2, True) #단순화

                    for pt in approx:
                        u, v = pt[0]
                        depth = depth_frame.get_distance(u, v)
                        X, Y, Z = rs.rs2_deproject_pixel_to_point(depth_intrinsics, [u, v], depth)
                        robot_path.append((X, Y, Z))

            output = color_image.copy()
            cv2.drawContours(output, filtered_contours, -1, (255, 255 , 0), 2)
            cv2.imshow("sans", output)

            if robot_path:
                print("로봇 경로 좌표:", robot_path[:10], "...")

            if cv2.waitKey(1) == 27:  # ESC
                break

    finally:
        pipeline.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()