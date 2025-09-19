import pose_estimator


if __name__== '__main__':
    input_path = ''
    output_path = ''

    cfg_path = ''
    ckpt_path = ''

    model = pose_estimator.initialize(cfg_path, ckpt_path)
    results = pose_estimator.inference(input_path, model)

    _ = pose_estimator.visualize(input_path, output_path, model, results)