import os
import sys
import cv2
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ultralytics import YOLO

sns.set_style("darkgrid")

image = cv2.imread("C:/Users/user/Desktop/Gunnu/Python/Programms/ODR_in_SatelliteImagery/dataset/ships-aerial-images/test/images/02e39612d_jpg.rf.cc5483bb711f080d12b644ff62cf977a.jpg")

train_imgs = "C:/Users/user/Desktop/Gunnu/Python/Programms/ODR_in_SatelliteImagery/dataset/ships-aerial-images/train/images"
train_labels = "C:/Users/user/Desktop/Gunnu/Python/Programms/ODR_in_SatelliteImagery/dataset/ships-aerial-images/train/labels"

test_imgs = "C:/Users/user/Desktop/Gunnu/Python/Programms/ODR_in_SatelliteImagery/dataset/ships-aerial-images/test/images"
test_labels = "C:/Users/user/Desktop/Gunnu/Python/Programms/ODR_in_SatelliteImagery/dataset/ships-aerial-images/test/labels"

val_imgs = "C:/Users/user/Desktop/Gunnu/Python/Programms/ODR_in_SatelliteImagery/dataset/ships-aerial-images/valid/images"
val_labels = "C:/Users/user/Desktop/Gunnu/Python/Programms/ODR_in_SatelliteImagery/dataset/ships-aerial-images/valid/labels"

height, width, channels = image.shape
print(f"Image Dimension : {height} X {width} and {channels} channels.")

# View random 16 Images in 4X4 format.

random_imgs = random.sample(train_imgs, 16)

fig, axs = plt.subplots(4, 4, figsize=(16, 16))

for i, img_file in enumerate(random_imgs):
    row = i // 4
    col = i % 4

    img_path = os.path.join(train_imgs, img_file)
    image = cv2.imread(img_path)

    label_file = os.path.splitext(img_file)[0] + ".txt"
    label_path = os.path.join(train_labels, label_file)

    with open(label_path, "r") as f:
        labels = f.read().strip().split("\n")

    for label in labels:
        if len(label.split()) != 5:
            continue

        class_id, x_center, y_center, width, height = map(float, label.split())
        x_min = int((x_center - width/2) * image.shape[1])
        y_min = int((y_center - height/2) * image.shape[0])
        x_max = int((x_center + width/2) * image.shape[1])
        y_max = int((y_center + height/2) * image.shape[0])
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)

    axs[row, col].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[row, col].axis('off')

plt.show()