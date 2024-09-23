import os
import random
import shutil

# Paths to your unzipped dataset
image_dir = r"C:\Users\User\PycharmProjects\image\images"  # Path to the images folder
label_dir = r"C:\Users\User\PycharmProjects\image\labels"  # Path to the labels folder

# Directory to save the split datasets inside the "image" folder
output_dir = r'C:\Users\User\PycharmProjects\image\dataset_split'
train_img_dir = os.path.join(output_dir, 'images', 'train')
val_img_dir = os.path.join(output_dir, 'images', 'val')
test_img_dir = os.path.join(output_dir, 'images', 'test')
train_label_dir = os.path.join(output_dir, 'labels', 'train')
val_label_dir = os.path.join(output_dir, 'labels', 'val')
test_label_dir = os.path.join(output_dir, 'labels', 'test')

# Create output directories if they don't exist
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(test_img_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)
os.makedirs(test_label_dir, exist_ok=True)

# List all image files
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]

# Shuffle the data to ensure randomness
random.seed(42)  # For reproducibility
random.shuffle(image_files)

# Define the split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Calculate the number of images for each split
total_images = len(image_files)
train_count = int(train_ratio * total_images)
val_count = int(val_ratio * total_images)

# Split the dataset
train_files = image_files[:train_count]
val_files = image_files[train_count:train_count + val_count]
test_files = image_files[train_count + val_count:]

# Function to copy files
def copy_files(file_list, source_img_dir, source_label_dir, dest_img_dir, dest_label_dir):
    for file_name in file_list:
        # Image file path
        src_img_path = os.path.join(source_img_dir, file_name)
        dest_img_path = os.path.join(dest_img_dir, file_name)

        # Label file path (replace .jpg or .png with .txt)
        label_name = file_name.rsplit('.', 1)[0] + '.txt'
        src_label_path = os.path.join(source_label_dir, label_name)
        dest_label_path = os.path.join(dest_label_dir, label_name)

        # Copy both image and label if they exist
        if os.path.exists(src_img_path) and os.path.exists(src_label_path):
            shutil.copy(src_img_path, dest_img_path)
            shutil.copy(src_label_path, dest_label_path)

# Copy the files to the respective directories
copy_files(train_files, image_dir, label_dir, train_img_dir, train_label_dir)
copy_files(val_files, image_dir, label_dir, val_img_dir, val_label_dir)
copy_files(test_files, image_dir, label_dir, test_img_dir, test_label_dir)

print(f"Training set: {len(train_files)} images")
print(f"Validation set: {len(val_files)} images")
print(f"Test set: {len(test_files)} images")
