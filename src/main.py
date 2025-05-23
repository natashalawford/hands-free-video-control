# Entry point to run the app

import sys
import time
import cv2
import mediapipe as mp
import gesture_controller
import threading
from ad_skipper import skip_ad_monitor
from voice_controller import voice_control

# CONSTANTS
COOLDOWN_TIME = 2  # seconds between gestures, prevents multiple triggers

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
                        static_image_mode=False, 
                        max_num_hands=1, 
                        min_detection_confidence=0.7,
                        min_tracking_confidence=0.7
                       )
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


def run_webcam():
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)
    last_time = 0  # last time a gesture was detected

    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    while True:
        # Capture frame-by-frame
        read, frame = cap.read()
        if not read:
            print("Error: frame is unreadable")
            break

        #Convert the frame to RGB for MediaPipe processing
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame and detect a single hand
        results = hands.process(frame_rgb)
        
        # Draw hand landmarks on the frame if hand is detected
        
        current_time = int(time.time())

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    # Add colours to different parts of the hand:
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

            # PAUSE/PLAY gesture detection
            if (current_time - last_time) > COOLDOWN_TIME and \
                gesture_controller.is_open_palm(hand_landmarks):
                # Trigger play/pause action here
                last_time = current_time

            # SPEED UP / SLOW DOWN gesture detection
            elif (current_time - last_time) > COOLDOWN_TIME and \
                gesture_controller.is_peace_sign(hand_landmarks) :
                # Trigger speed up / slow down action here
                last_time = current_time

            # VOLUME UP / VOLUME DOWN gesture detection
            elif (current_time - last_time) > COOLDOWN_TIME and \
                gesture_controller.thumbs_up(hand_landmarks):
                # Trigger volume up action here
                last_time = current_time

            # SKIP gesture detection
            elif (current_time - last_time) > COOLDOWN_TIME and \
                gesture_controller.is_finger_pointing(hand_landmarks):
                # Trigger skip action here
                last_time = current_time


        # Display the each frame:
        cv2.imshow('Hands Free Video Control - Webcam Feed',  cv2.flip(frame, 1))

        # Break the loop / exit webcam when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #If 'q' is pressed or frame error occurs, close webcam all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    ad_skipper_thread = threading.Thread(target=skip_ad_monitor, daemon=True)
    ad_skipper_thread.start()

    voice_thread = threading.Thread(target=voice_control, daemon=True)
    voice_thread.start()

    run_webcam()
    