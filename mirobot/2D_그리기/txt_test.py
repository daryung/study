import numpy as np
from path_yolo import yolo_segmentation_realsense_once
from robot_path_conv import pixel_to_robot

if __name__ == "__main__":
    all_paths = yolo_segmentation_realsense_once()
    robot_paths = pixel_to_robot(all_paths)

    with open("robot_commands.txt", "w") as f:
        for obj_idx, path in enumerate(robot_paths):
            f.write(f"# 객체 {obj_idx+1}\n")
            for x, y in path:
                f.write(f"{x:.2f}, {y:.2f}\n")
            f.write("\n")

    print("robot_commands.txt 파일이 생성되었습니다.")