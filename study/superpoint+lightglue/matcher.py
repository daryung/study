import torch
from lightglue import LightGlue, SuperPoint
from lightglue.utils import load_image, rbd
from lightglue import viz2d


def compute_correspondence_matching(src_path, dst_path, max_kpts=2048):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    extractor = SuperPoint(max_num_keypoints=max_kpts).eval().to(device)
    matcher = LightGlue(features="superpoint").eval().to(device)
    
    src_image = load_image(src_path).to(device)
    dst_image = load_image(dst_path).to(device)
    
    src_features = extractor.extract(src_image)
    dst_features = extractor.extract(dst_image)
    
    matches = matcher({'image0': src_features, 'image1': dst_features})
    
    src_features, dst_features, matches = [
        rbd(x) for x in [src_features, dst_features, matches]
    ]
    
    src_kpts = src_features["keypoints"]
    dst_kpts = dst_features["keypoints"]
    match_result = matches["matches"]
    
    matched_src_kpts = src_kpts[match_result[..., 0]]
    matched_dst_kpts = dst_kpts[match_result[..., 0]]
    
    src_results = matched_src_kpts.cpu().numpy()
    dst_results = matched_dst_kpts.cpu().numpy()
    
    return src_results, dst_results

def visualize(src_path, dst_path, src_kpts, dst_kpts):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    original_img0 = load_image(src_path).to(device)
    original_img1 = load_image(dst_path).to(device)

    axes = viz2d.plot_images([original_img0, original_img1])

    viz2d.plot_matches(src_kpts, dst_kpts, color="lime", lw=0.2)
    viz2d.save_plot('result.png')

import matcher

if __name__ == "__main__":
    src_path = "phototourism/british_museum/08004508_282791427.jpg"
    dst_path = "phototourism/british_museum/30495805_5912735553.jpg"

    src_kpts , dst_kpts = matcher.compute_correspondence_matching(src_path, dst_path)
    matcher.visualize(src_path,dst_path,src_kpts,dst_kpts)
