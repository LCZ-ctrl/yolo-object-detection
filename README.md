# YOLO Object Detection

This is a repo about modified YOLO modles written in PyTorch from scratch, and it's also the first time I try to
implement an object detection model myself.  
I'm using `PyTorch 2.10.0+cu128` in `Python 3.12.0`.

| Model  | Params | Epochs | Time  | Input Size  | Test Size | mAP@0.5 | mAP@0.6 | mAP@0.75 |
|:-------|--------|:-------|-------|:------------|:----------|:--------|:--------|:---------|
| YOLOv1 | 21.29M | 150    | 3.11h | multi-scale | 640x640   | 76.02%  | 70.10%  | 50.27%   |
| YOLOv2 | 30.90M | 150    | 3.59h | multi-scale | 640x640   | 79.09%  | 74.13%  | 54.80%   |

## Requirements

```
matplotlib==3.10.8
numpy==2.4.3
opencv_python==4.13.0.92
torch==2.10.0+cu128
torchvision==0.25.0+cu128
tqdm==4.67.3
```

## Dataset

The dataset comes from PASCAL VOC 2007 and
2012: [PASCAL VOC](https://www.kaggle.com/datasets/vijayabhaskar96/pascal-voc-2007-and-2012). It has a total of 20
categories.  
I used VOC2007 trainval + VOC2012 trainval to train the model (about 16,551 images) and VOC2007 test to evaluate the
model's performance (about 4,952 images).  
*JPEGImages* folder includes original images; *Annotations* folder includes annotation files for each image; *ImageSets*
folder recorded the split information of the dataset.

## Train

To start training, run the command -

```
python train.py
```

I used Automatic Mixed Precision (AMP) to accelerate the training process and reduce memory consumption without
sacrificing numerical precision. Furthermore, I used a Cosine Annealing scheduler with a linear warm-up phase during
training. Additionally, Multi-scale Training was implemented, where the input image resolution was randomly sampled
every epoch.

You can adjust hyperparameters in ```config.py``` according to your own hardware (It is recommended to train on a GPU).
I used an NVIDIA GeForce RTX 5090 GPU (32GB VRAM).

<strong>*My trained weights:*</strong> [YOLO](https://huggingface.co/LCZ-ctrl/yolo-object-detection)

## Test

To test your trained model, run the command -

```
python test.py
```

It will randomly select an image in the test set, and then output the model's prediction results. You can also try your
own images!

## Results

*Images it had never seen before*:  
<br>
<p align="center">
  <img src="./yolov1/images/911.png" height="200" />
  <img src="./yolov1/images/plane.png" height="200" />
  <br>
  <img src="./yolov1/images/motor.png" height="200" />
  <img src="./yolov1/images/federer.png" height="200" />
  <br>
  <em><strong>YOLOv1 Results</strong></em>
</p>
<br>
<p align="center">
  <img src="./yolov2/images/senna.png" height="200" />
  <img src="./yolov2/images/cat.png" height="200" />
  <br>
  <img src="./yolov2/images/swan.png" height="200" />
  <img src="./yolov2/images/ski.png" height="200" />
  <br>
  <em><strong>YOLOv2 Results</strong></em>
</p>

## Acknowledgement

This repo is inspired by [RT-ODLab](https://github.com/yjh0410/RT-ODLab). Thanks for the excellent works.
