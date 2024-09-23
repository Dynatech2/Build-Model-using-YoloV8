from ultralytics import YOLO


def train_model(config):
    # Load the model
    model = YOLO('yolov8n.pt')  # Use your pre-trained model or architecture file

    # Train the model
    results = model.train(
        data=config['data'],
        epochs=config['epochs'],
        batch=config['batch'],
        imgsz=config['imgsz'],
        save=True,  # Save model checkpoints
        project=config['project'],  # Directory to save results
        name=config['name']  # Experiment name
    )

    # Print the directory where the model is saved
    print(f"Model saved at: {results.save_dir}")

    return results

def main():
    # Define your training configuration
    config = {
        'data': '/home/dyna/PycharmProjects/DYNAPROJECT/vehicledataset5_combined/data.yaml',
        'epochs': 200,
        'batch': 16,
        'imgsz': 1280,
        'save': True,
        'project': 'runs/train',
        'name': 'vehicle_detection'
    }

    # Train the model
    train_results = train_model(config)
    print(f"Training results:\n{train_results}")

if __name__ == "__main__":
    main()
