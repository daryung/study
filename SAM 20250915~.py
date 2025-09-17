from mmdet.apis import DetInferencer

def initalize (cfg_path, ckpt_path, device):
    return DetInferencer(
        model = cfg_path,
        wights = ckpt_path,
        device = device,
        show_progress=False)


def inference (input_path, model):
    results = model(
        inputs=input_path,
        out_dir= None,
        no_save_vis=True,
        pred_score_thr = 0.75)

    return results['predictions'][0]

# 1. cd weights
# 2. wget https://download.openlab.com/mmdetection/v3.0/detr/detr_r50_8xb2-150e_coco/dete_r50_8xb2-150e_coco_20221023_153551-436d03e8.pth


#######################################


import cv2
import numpy as np
from segment_anything import SamPreditor , sam_model_registry

def intialize(model_type, ckpt_path) :
    model = sam_model_registry[model_type](checkpoint=ckpt_path)
    predictor = SamPredictor(model)

    return predictor

#wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth

def inference (input_path, prompt_bbox, predictor):
    input_img = cv2.imread(input_path)
    preditor.set_image(input_img)

    bbox = np.array(prompt_box)  

    mask, scores, _ = predictor.predict(box=bbox, multimask_output = False) #지정한 박스 영역을 기준으로 마스크 예측

    result_mask = masks[np.argmax(scores)]

    return result_mask

def visualize(input_img, input_mask, mask_color):
    overlat mask = input_img.copy()
    overlay_mask[input_mask] = mask_color

    alpha = 0.5
    overlay_mask = cv2.addWeighted(input_img, 1-alpha, overlay_mask, alpha, 0)

    return overlay_mask

    


        
