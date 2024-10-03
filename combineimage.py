import os
import shutil


def copy_files(src_folders, dest_folder):
    # Define subfolders for train, val, test in both images and labels
    categories = ['train', 'val', 'test']
    for category in categories:
        images_dest_folder = os.path.join(dest_folder, 'images', category)
        labels_dest_folder = os.path.join(dest_folder, 'labels', category)

        # Create the subfolders if they don't exist
        os.makedirs(images_dest_folder, exist_ok=True)
        os.makedirs(labels_dest_folder, exist_ok=True)

    for src_folder in src_folders:
        # Walk through all subfolders in the source directory
        for root, dirs, files in os.walk(src_folder):
            for file_name in files:
                # Determine source file path
                src_file_path = os.path.join(root, file_name)

                # Determine if the file is an image or label based on its extension
                if file_name.endswith('.jpg') or file_name.endswith('.png'):  # Image files
                    if 'train' in root:
                        target_folder = os.path.join(dest_folder, 'images', 'train')
                    elif 'val' in root:
                        target_folder = os.path.join(dest_folder, 'images', 'val')
                    elif 'test' in root:
                        target_folder = os.path.join(dest_folder, 'images', 'test')
                    else:
                        continue  # Skip if folder is not in train/val/test
                elif file_name.endswith('.txt'):  # Label files
                    if 'train' in root:
                        target_folder = os.path.join(dest_folder, 'labels', 'train')
                    elif 'val' in root:
                        target_folder = os.path.join(dest_folder, 'labels', 'val')
                    elif 'test' in root:
                        target_folder = os.path.join(dest_folder, 'labels', 'test')
                    else:
                        continue  # Skip if folder is not in train/val/test
                else:
                    continue  # Skip if the file is neither an image nor a label

                # Determine destination file path
                dest_file_path = os.path.join(target_folder, file_name)

                # Check if a file with the same name already exists in the destination
                if os.path.exists(dest_file_path):
                    base_name, ext = os.path.splitext(file_name)
                    counter = 1
                    # Create a unique file name by appending a number
                    while os.path.exists(dest_file_path):
                        dest_file_path = os.path.join(target_folder, f"{base_name}_{counter}{ext}")
                        counter += 1

                # Copy the file to the target folder
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied {src_file_path} to {dest_file_path}")

    print("Files have been successfully copied and organized.")


# Define the list of source folders
src_folders = [
    '/media/dyna/506AE4B56AE498CC/pycharm-community-2024.2.2/PycharmProjects/DYNAPROJECT/vehicledataset',  # First folder
    '/media/dyna/506AE4B56AE498CC/pycharm-community-2024.2.2/PycharmProjects/DYNAPROJECT/vehicledataset2s',  # Second folder
    '/media/dyna/506AE4B56AE498CC/pycharm-community-2024.2.2/PycharmProjects/DYNAPROJECT/vehicledataset3'  # Third folder
]

# Define the destination folder
dest_folder = '/media/dyna/506AE4B56AE498CC/pycharm-community-2024.2.2/PycharmProjects/DYNAPROJECT/vehicledataset12'  # Destination folder

# Copy files from all source folders
copy_files(src_folders, dest_folder)

print("Copying from multiple folders complete.")
