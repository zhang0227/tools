from mmdet.apis import init_detector, inference_detector, show_result
import mmcv
import numpy as np
import glob
import os

config_file = 'configs/cat_dog_faster_rcnn_r50_fpn_1x.py'
checkpoint_file = 'work_dirs/cat_dog_faster_rcnn_r50_fpn_1x/latest.pth'
score_thr = 0.9

# 通过配置文件（config file）和模型文件（checkpoint file）构建检测模型
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# 测试单张图片
# img = '/data1/Projects/datasets/cat_dog_single/cat.12176.jpg'
# result = inference_detector(model, img)
# show_result(img, result, model.CLASSES, score_thr=score_thr,
#             out_file='/data1/Projects/datasets/cat_dog_single/res_cat.12176.jpg')

# 测试多张图片

# imgs = glob.glob('/data1/Projects/datasets/coco/val2017/*.jpg')
imgs = glob.glob('/data1/Projects/datasets/test/*.jpg')
for i, img in enumerate(imgs):
    # 画 bounding boxes 到图片上
    # print(i, imgs[i])
    result = inference_detector(model, img)
    file_name = imgs[i].split('/')[-1]
    out_file = os.path.join('/data1/Projects/datasets/test_det', file_name)
    show_result(img, result, model.CLASSES, score_thr=score_thr, show = False,out_file=out_file)

    # 输出图片的猫和狗的数量
    img = mmcv.imread(img)
    img = img.copy()
    bbox_result = result
    bboxes = np.vstack(bbox_result)
    labels = [
        np.full(bbox.shape[0], i, dtype=np.int32)
        for i, bbox in enumerate(bbox_result)
    ]
    labels = np.concatenate(labels)

    # 根据阈值调整输出的 bboxes 和 labels
    scores = bboxes[:, -1]
    inds = scores > score_thr
    bboxes = bboxes[inds, :]
    labels = labels[inds]

    class_names = model.CLASSES
    cat_dog_dict = {}
    for label in labels:
        cat_dog_dict[class_names[label]] = cat_dog_dict.get(class_names[label], 0) + 1
    for k, v in cat_dog_dict.items():
        print('{0} 有 {1}  {2}'.format(imgs[i].split('/')[-1], v, k))
    print('--------------------')
