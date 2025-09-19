def inference_one_frame(input_frame, model):
    batch_results = inference_topdown(model, input_frame)
    results = merge_data_samples(batch_results)

    return results

def inference_and_save_video(input_path, output_path, model):
    model.cfg.visualizer.radius = 4
    model.cfg.visualizer.alpha = 0.9
    model.cfg.visualizer.line_width = 1

    visualizer = VISUALIZERS.build(model.cfg.visualizer)
    visualizer.set_dataset_meta(model.dataset_meta, skeleton_style='mmpose')

    video_cap = cv2.VideoCapture(input_path)
    video_writer = None

    while video_cap.isOpened():
        success, video_frame = video_cap.read()
        if not success:
            break

        results = inference_one_frame(video_frame, model)
        visualizer.add_datasample(
            'result',
            video_frame,
            data_sample=results,
            draw_gt=False,
            draw_heatmap=False,
            draw_bbox=False,
            show_kpt_idx=True,
            skeleton_style='mmpose',
            show=False,
            kpt_thr=0.7)

        frame_vis = visualizer.get_image()

        if video_writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video_writer = cv2.VideoWriter(output_path, fourcc, 30, (frame_vis.shape[1], frame_vis.shape[0]))

        video_writer.write(frame_vis)

    if video_writer:
        video_writer.release()

    video_cap.release()