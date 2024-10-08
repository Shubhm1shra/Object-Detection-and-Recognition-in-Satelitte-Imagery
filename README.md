# Object-Detection-and-Recognition-in-Satelitte-Imagery

This repository provides a comparitive analysis of three popular object detection models - YOLOv8, FasterRCNN, and RetinaNet - on satellite imagery data from [Kaggle](https://www.kaggle.com/datasets/siddharthkumarsah/ships-in-aerial-images). The aim is to evaluate the model's performance, efficiency, and accuracy to determine the most suitable approach for object detection in satellite images.

## Table of Contents
* Overview
* Dataset
* Models
* Installation
* Usuage
* Results
* Contributions
* License

## Overview
Satellite Imagery has unique challenges for object detection, such as varied scales, complex backgrounds, and sometimes low resolutions. This project compares YOLOv8, FasterRCNN, and RetinaNetyo identify the model best suited for accurate object detection in satellite images.

## Dataset
The Dataset used for this analysis is composed of high-resolution satellite images with annotated images of ships and vessels in sea/ocean taken from [Kaggle](https://www.kaggle.com/datasets/siddharthkumarsah/ships-in-aerial-images). The images are divided into training, testing and validation dataset to enable a comprehensive evaluation of each model.

## Models
The following models are used in this analysis:
1. YOLOv8 : Known for its speed and efficiency, YOLOv8 is a real time object detection model suitable for various applications, including those with limited resources.
2. FasterRCNN : A region-based nidek providing high accuracy with slower speeds, particularly well-suited for complex-images.
3. RetinaNet : Utilizes focal loss to handle class imbalance, often encountered in object detection tasks like satellite imagery analysis.
Each model is trained with specific configurations to optimize performance.

## Installation
Clone this repository and install the required dependencies.

`git clone https://github.com/Shubhm1shra/Object-Detection-and-Recognition-in-Satellite-Imagery.git`

`cd Object-Detection-and-Recognition-in-Satellite-Imagery`
## Usage
1. **Data Preparation :** Ensure that the dataset is correctly formatted and placed in the data/directory. Update any paths in the configuration files if necessary.
2. **Trainging the Model :**
    * YOLOv8 : Individual cell segments for training  in YOLO ipynb file needs to be run.
    * FasterRCNN : Individual cell segments for training  in FasterRCNN ipynb file needs to be run.
    * RetinaNet : Individual cell segments for training  in RetinaNet ipynb file needs to be run.
3. **Testing the Model :** For any model testing, run the cell segment for the same in the individual file.
4. **Comparision and Analysis :** After validation, the results for each model are saved and can be visualized or compared through metrics such as Intersection over Union (IoU) , Mean Average Precision (mAP), inference time, and more.
## Results
## Contribution
Contribution are welcome! Please create an issue ir pull request if you would like to add new feature or improvements.
## License
The Project is licensed under the MIT License. See the License file for details.
