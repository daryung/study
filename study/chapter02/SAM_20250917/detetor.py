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
    
    predictions = results['predictions'][0]
    valid_indices = [i for i, score in enumerate(preditions['score']) if score >= 0.75]
    valid_bboxes = [predictions['bboxes'][i] for i in valid_indices]

    return valid_bboxes

# 1. cd weights
# 2. wget https://download.openlab.com/mmdetection/v3.0/detr/detr_r50_8xb2-150e_coco/dete_r50_8xb2-150e_coco_20221023_153551-436d03e8.pth

