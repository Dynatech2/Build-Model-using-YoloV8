from ultralytics import YOLO
import os

def evaluate_model(model_path, val_data):
    # Check if the model path exists
    if not os.path.exists(model_path):
        print(f"Error: Model path does not exist: {model_path}")
        return

    # Load the trained model
    model = YOLO(model_path)

    # Perform validation
    results = model.val(data=val_data)

    # Print validation results
    print(f"Validation results:\n{results}")

def main():
    # Define the model path and validation data
    model_path = '/home/dyna/PycharmProjects/DYNAPROJECT/runs/train/vehicle_detection64/weights/best.pt'
    val_data = '/home/dyna/PycharmProjects/DYNAPROJECT/vehicledataset7/data.yaml'

    # Evaluate the model
    evaluate_model(model_path, val_data)

if __name__ == "__main__":
    main()
