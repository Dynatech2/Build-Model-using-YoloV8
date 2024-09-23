# YOLOv8 Image Training Project

This repository provides instructions on how to set up and train a YOLOv8 model using custom image datasets. It includes step-by-step guidance on creating a project in PyCharm, setting up the necessary environment, splitting the dataset, training the model, and checking dependencies.

## Table of Contents

- [Installation](#installation)
- [Project Setup](#project-setup)
- [Dataset Preparation](#dataset-preparation)
- [Training the YOLOv8 Model](#training-the-yolov8-model)
- [Results and Evaluation](#results-and-evalution)
- [Check Dependency Versions](#check-dependency-version)
- [References](#references)

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
   
