'''
import cv2
import torch

# Load the YOLOv8 model.
model = torch.hub.load("ultralytics/yolov8:latest", "yolov8-tiny")

# Create a video capture object to access the camera.
cap = cv2.VideoCapture(0)

while True:

    # Read a frame from the video.
    ret, frame = cap.read()

    # If the frame was not read, break the loop.
    if not ret:
        break

    # Detect objects in the frame.
    results = model(frame)

    # Display the results on the screen.
    cv2.imshow("YOLOv8 Object Detection", results)

    # Check if the user pressed the escape key to exit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object.
cap.release()

# Close the windows.
cv2.destroyAllWindows()

'''