# Entry point to run the app

import cv2

def run_webcam():
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    while True:
        # Capture frame-by-frame
        read, frame = cap.read()
        if not read:
            print("Error: frame is unreadable")
            break

        # Display the each frame:
        cv2.imshow('Hands Free Video Control - Webcam Feed', frame)

        # Break the loop / exit webcam when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #If 'q' is pressed or frame error occurs, close webcam all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_webcam()