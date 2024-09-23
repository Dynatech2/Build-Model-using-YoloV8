from ultralytics import YOLO


def train_model(config):
    # Load the model
    model = YOLO('yolov8n.pt')  # Load YOLOv8n model or replace with desired variant

    # Train the model
    results = model.train(
        data=config['data'],
        epochs=config['epochs'],
        batch=config['batch'],
        imgsz=config['imgsz'],
        project=config['project'],  # Directory to save results
        name=config['name']  # Experiment name
    )

    # Print the directory where the model is saved
    print(f"Model saved at: {results.save_dir}")

    return results


def main():
    # Define your training configuration
    config = {
        'data': '/home/dyna/PycharmProjects/DYNAPROJECT/vehicledataset3/data.yaml',
        'epochs': 200,
        'batch': 16,
        'imgsz': 1280,
        'project': 'runs/train',
        'name': 'vehicle_detection'
    }

    # Train the model
    train_results = train_model(config)
    print(f"Training results:\n{train_results}")


if __name__ == "__main__":
    main()
