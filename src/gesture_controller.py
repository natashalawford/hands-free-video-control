# Handles webcam: hand and face detection

#CONSTANTS:

# Mediapipe allocated finger coordinates
THUMB_BASE = 3
INDEX_BASE = 6
MIDDLE_BASE = 10
RING_BASE = 14
PINKY_BASE = 18

THUMB_TIP = 4
INDEX_TIP = 8
MIDDLE_TIP = 12
RING_TIP = 16
PINKY_TIP = 20

def is_open_palm(hand_landmarks):
    fingers_up = 0
    finger_tips = [THUMB_TIP, INDEX_TIP, MIDDLE_TIP, RING_TIP, PINKY_TIP]
    finger_bases = [THUMB_BASE, INDEX_BASE, MIDDLE_BASE, RING_BASE, PINKY_BASE]

    for tip, base in zip(finger_tips, finger_bases):
        # Check if the tip is above the base in y-coordinates
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[base].y:
            fingers_up += 1

    return fingers_up == 5
