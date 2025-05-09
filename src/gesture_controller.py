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

def is_peace_sign(hand_landmarks):
    # Check if the index and middle fingers are up and the rest are down
    index_up = hand_landmarks.landmark[INDEX_TIP].y < hand_landmarks.landmark[INDEX_BASE].y
    middle_up = hand_landmarks.landmark[MIDDLE_TIP].y < hand_landmarks.landmark[MIDDLE_BASE].y
    ring_down = hand_landmarks.landmark[RING_TIP].y > hand_landmarks.landmark[RING_BASE].y
    pinky_down = hand_landmarks.landmark[PINKY_TIP].y > hand_landmarks.landmark[PINKY_BASE].y

    return index_up and middle_up and ring_down and pinky_down

def is_downward_peace_sign(hand_landmarks):
    # Check if the index and middle fingers are up and the rest are down
    index_up = hand_landmarks.landmark[INDEX_TIP].y > hand_landmarks.landmark[INDEX_BASE].y
    middle_up = hand_landmarks.landmark[MIDDLE_TIP].y > hand_landmarks.landmark[MIDDLE_BASE].y
    ring_down = hand_landmarks.landmark[RING_TIP].y < hand_landmarks.landmark[RING_BASE].y
    pinky_down = hand_landmarks.landmark[PINKY_TIP].y < hand_landmarks.landmark[PINKY_BASE].y

    return index_up and middle_up and ring_down and pinky_down