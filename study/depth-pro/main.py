import cv2
import torch 
import numpy as np 

import depth_pro


#가상환경 한 후 실행 권장, 같은 디렉토리에 모델 깔아서 함


input_path = "data/example.jpg"
output_depth_path = "results/depth.npy"
output_depth_vis_path = "results/depth_vis3.jpg"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

depth_model, transfrom = depth_pro.create_model_and_transforms(device=device, precision=torch.float16)
depth_model.eval()

input_img, _, focal_px = depth_pro.load_rgb(input_path)
input_img = transfrom(input_img)

result = depth_model.infer(input_img, f_px=focal_px)

print(result)

output_depth = result["depth"].cpu().numpy()
output_depth = output_depth * 1000.0
output_focal_px = result["focallength_px"].cpu().numpy()

depth_vis_img = np.uint8(cv2.normalize(output_depth, None, 0, 255, cv2.NORM_MINMAX))

np.save(output_depth_path, output_depth)
cv2.imwrite(output_depth_vis_path, depth_vis_img)


