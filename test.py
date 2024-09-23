from ultralytics import YOLO
import cv2



def get_color(class_id):
    # Define a color palette for 6 classes (BGR format for OpenCV)
    colors = [
        (255, 0, 0),     # Blue
        (0, 255, 0),     # Green
        (0, 0, 255),     # Red
        (255, 255, 0),   # Cyan
        (255, 0, 255),   # Magenta
        (0, 255, 255)    # Yellow
    ]
    return colors[class_id % len(colors)]

def draw_custom_labels(frame, results):
    for result in results:
        for box in result.boxes:
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Get class label and confidence score
            class_id = int(box.cls[0])
            label = f"{result.names[class_id]} {box.conf[0]:.2f}"

            # Get color for the class
            color = get_color(class_id)

            # Draw bounding box with thin line (thickness = 1)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 4)

            # Draw label background (default size)
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.75, 1)
            background_padding = 1  # Small padding around the text
            cv2.rectangle(frame, (x1, y1 - h - 2 * background_padding), (x1 + w + 2 * background_padding, y1), color, -1)

            # Draw label text (default size, white color)
            cv2.putText(frame, label, (x1 + background_padding, y1 - background_padding), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    return frame

def test_model_on_rtsp_stream(model_path, rtsp_url):
    # Load the trained model
    model = YOLO(model_path)

    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Error: Cannot open RTSP stream")
        return

    # Set the frame resolution to 640x480
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Create a named window
    cv2.namedWindow("RTSP Stream - Vehicle Detection", cv2.WND_PROP_FULLSCREEN)

    # Set the window to full screen
    cv2.setWindowProperty("RTSP Stream - Vehicle Detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Run detection on the frame
        results = model(frame)

        # Visualize the results with custom labels
        annotated_frame = draw_custom_labels(frame, results)

        # Display the frame in full screen
        cv2.imshow("RTSP Stream - Vehicle Detection", annotated_frame)

        # Exit loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the stream and close windows
    cap.release()
    cv2.destroyAllWindows()

def main():
    # Define the model path and RTSP stream URL
    model_path = '/home/dyna/PycharmProjects/DYNAPROJECT/runs/train/vehicle_detection64/weights/best.pt'
    rtsp_url = 'rtsp://admin:Dyna1234@180.74.167.65:551/stream0'

    # Test the model on the RTSP stream
    test_model_on_rtsp_stream(model_path, rtsp_url)

if __name__ == "__main__":
    main()

