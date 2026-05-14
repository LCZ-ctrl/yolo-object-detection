import torch
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'cpu'
img_size = 640
num_classes = 20
num_workers = 4
batch_size = 16
max_epoch = 100
wp_epoch = 2
pretrained = True

lr = 1e-3
momentum = 0.937
weight_decay = 5e-4
model_name = 'resnet18'

obj_weight = 1.0
cls_weight = 1.0
box_weight = 5.0

root = 'data/VOCdevkit/'
train_sets = [('2007', 'trainval'), ('2012', 'trainval')]
val_sets = [('2007', 'test')]

save_folder = 'weights/'
conf_thresh = 0.005
nms_thresh = 0.6

use_amp = True
multi_scale_sizes = [384, 416, 448, 480, 512, 544, 576, 608, 640, 672, 704, 736, 768, 800]
