# YOLOv8 Image Training Project

This repository provides instructions on how to set up and train a YOLOv8 model using custom image datasets. It includes step-by-step guidance on creating a project in PyCharm, setting up the necessary environment, splitting the dataset, training the model, and checking dependencies.

## Table of Contents

- [Installation](#installation)
- [Project Setup](#project-setup)
- [Dataset Preparation](#dataset-preparation)
- [Training the YOLOv8 Model](#training-the-yolov8-model)
- [Evaluating the Model](#evaluating-the-model)
- [Results and Evaluation](#results-and-evalution)
- [References](#references)
- [Testing the Model on RTSP Stream](testing-the-model-on-rtsp-stream)

---

## Installation

1. **Install Python and PyCharm**
   Ensure you have Python 3.8 or higher and PyCharm installed as your IDE. You can download Python from [here](https://www.python.org/downloads/).

2. **Install Ultralytics**
   You only need to install Ultralytics to set up YOLOv8. This will also automatically install PyTorch and any required dependencies.
   
   Run the following command in your terminal:

   ```
   pip install ultralytics
   ```
3. **Verify Installation**
    You can verify that Ultralytics has been installed successfully by checking the version:
   ```
   pip show ultralytics
   ```
   If you want to check the PyTorch version (which is installed as part of Ultralytics):
   ```
   pip show torch
   ```
   If you want to check CUDA version:
   ```
   nvidia-smi
   ```
   The versions we are using are:
   - ultralytics=8.2.79
   - CUDA=12.6
   - torch=2.4.0
   - torvision=0.19.0
----

## Project Setup

1. **Create a New Project in PyCharm**
   - Open **PyCharm** and select **File > New Project**.
   - Name your project (e.g., training) and choose a location for your project files.

2. **Set Up Virtual Environment (Project venv)**
   - Go to File > Settings > Project > Python Interpreter.
   - Click on Add Interpreter.
   - Choose the Project venv option:
   - This will create a virtual environment for your project and isolate dependencies.

Once your virtual environment is set up, you can install the required packages by running:
   ```
   pip install ultralytics
   ```
----
## Dataset Preparation

1. **Split the Dataset First**
   Use the provided Python script [splitimages.py](https://github.com/Dynatech2/Build-Model-using-YoloV8/blob/main/splitimages.py) to split your dataset into training (80%), validation (10%), and testing (10%) sets. This script will organize your images and labels into their respective directories.

2. **Create Dataset Configuration File**
   After splitting the dataset, create a **data.yaml** file to define the paths to the training, validation, and testing datasets, as well as the class names. The **data.yaml** file should look like this:
   ```
   train: ./path/to/train/images
   val: ./path/to/valid/images
   test: ./path/to/test/images

   nc: 6  # number of classes
   names: ['class1', 'class2', 'class3', 'class4', 'class5', 'class6']
   ```
   Replace the paths with the actual locations of your datasets.
   
3. **Directory Structure After Splitting**
   After running the splitting script, your dataset should be structured like this:

   ```
   dataset_split/
   ├── images/
   │   ├── train/
   │   ├── val/
   │   └── test/
   └── labels/
       ├── train/
       ├── val/
       └── test/
   ```
 ----

 ## Training Configuration

 1. **Training Script**
    Use the existing [training.py](https://github.com/Dynatech2/Build-Model-using-YoloV8/blob/main/training.py) script to start training the YOLOv8 model.

2. **Training Parameters**
   Configure the parameters in training.py as needed. For a comprehensive list of all parameters and hyperparameters you can change, please refer to the [Ultralytics documentation](https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings).

3. **Model Saving Location**
   The trained model will be saved in the directory specified in your training configuration. In the provided script, the default saving path is:
   ```
   runs/train/vehicle_detection/
   ```
   This directory will contain the model weights, evaluation metrics, and logs

---

## Evaluating the Model

After training completes, the results (such as weights, evaluation metrics, and logs) will be saved in the specified project directory.

To evaluate the trained model, you can run validation code in [validate.py](https://github.com/Dynatech2/Build-Model-using-YoloV8/blob/main/validate.py)

Make sure to update the model_path and val_data variables with the correct paths for your trained model and validation dataset.

---

## Results and Evaluation

After the training and evaluation processes are complete, you can analyze the results to understand the model's performance better. During evaluation, the following metrics will be printed to the console:

1. Precision: Indicates the accuracy of positive predictions.
2. Recall: Measures the model's ability to capture all positive instances.
3. mAP (mean Average Precision): Average precision across classes, reflecting overall model performance.

---
## Testing the Model on RTSP Stream

You can test the trained YOLOv8 model using an RTSP stream by running the[test.py](https://github.com/Dynatech2/Build-Model-using-YoloV8/blob/main/test.py) script. This script captures the stream, performs object detection, and displays the results in real-time.

**Exit the Stream**
To stop the stream at any time, simply press 'q'.

---
## References
- [Ultralytics dependecies](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml)
- 


