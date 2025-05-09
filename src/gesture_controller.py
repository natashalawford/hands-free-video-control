# Handles webcam: hand and face detection

#CONSTANTS:

# Mediapipe allocated finger coordinates

# Thumb
THUMB_BASE = 1
THUMB_MCP = 2
THUMB_IP = 3
THUMB_TIP = 4

# Index
INDEX_BASE = 5
INDEX_PIP = 6
INDEX_DIP = 7
INDEX_TIP = 8

# Middle
MIDDLE_BASE = 9
MIDDLE_PIP = 10
MIDDLE_DIP = 11
MIDDLE_TIP = 12

# Ring
RING_BASE = 13
RING_PIP = 14
RING_DIP = 15
RING_TIP = 16

# Pinky
PINKY_BASE = 17
PINKY_PIP = 18
PINKY_DIP = 19
PINKY_TIP = 20

# Wrist
WRIST = 0

#PAUSE / PLAY
def is_open_palm(hand_landmarks):
    fingers_up = 0
    finger_tips = [THUMB_TIP, INDEX_TIP, MIDDLE_TIP, RING_TIP, PINKY_TIP]
    finger_middle = [THUMB_IP, INDEX_PIP, MIDDLE_PIP, RING_PIP, PINKY_PIP]
    finger_bases = [THUMB_BASE, INDEX_BASE, MIDDLE_BASE, RING_BASE, PINKY_BASE]

    for tip, middle, base in zip(finger_tips, finger_middle, finger_bases):
        # Check if the tip is above the base in y-coordinates
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[middle].y and hand_landmarks.landmark[middle].y < hand_landmarks.landmark[base].y + 0.1:
            fingers_up += 1

    return fingers_up == 5

# SPEED UP / SLOW DOWN
def is_peace_sign(hand_landmarks):
    # Check if the index and middle fingers are up and the rest are down
    index_up = hand_landmarks.landmark[INDEX_TIP].y < hand_landmarks.landmark[INDEX_PIP].y < hand_landmarks.landmark[INDEX_BASE].y
    middle_up = hand_landmarks.landmark[MIDDLE_TIP].y < hand_landmarks.landmark[MIDDLE_PIP].y < hand_landmarks.landmark[MIDDLE_BASE].y

    index_down = hand_landmarks.landmark[INDEX_TIP].y > hand_landmarks.landmark[INDEX_PIP].y > hand_landmarks.landmark[INDEX_BASE].y
    middle_down = hand_landmarks.landmark[MIDDLE_TIP].y > hand_landmarks.landmark[MIDDLE_PIP].y > hand_landmarks.landmark[MIDDLE_BASE].y

    ring_down = hand_landmarks.landmark[RING_TIP].y > hand_landmarks.landmark[RING_PIP].y
    pinky_down = hand_landmarks.landmark[PINKY_TIP].y > hand_landmarks.landmark[PINKY_PIP].y

    # Check to make sure thumb is down for downward peace sign
    thumb_down = hand_landmarks.landmark[THUMB_TIP].y > hand_landmarks.landmark[THUMB_IP].y > hand_landmarks.landmark[THUMB_BASE].y

    if index_up and middle_up and ring_down and pinky_down:
        print("Peace sign detected: triggering speed up")
        return True
    
    # The oppisite applies for the downward peace sign (Slow down detection)
    elif index_down and middle_down and not ring_down and not pinky_down and thumb_down:
        print("Downward peace sign detected: triggering slow down")
        return True
    
    return False

# VOLUME UP / VOLUME DOWN
def thumbs_up(hand_landmarks):
    # Check if the thumb is up and the rest  curled down
        # Thumb is up (all joints descending in Y)
    thumb_tip_y = hand_landmarks.landmark[THUMB_TIP].y
    thumb_ip_y = hand_landmarks.landmark[THUMB_IP].y
    thumb_mcp_y = hand_landmarks.landmark[THUMB_MCP].y
    thumb_base_y = hand_landmarks.landmark[THUMB_BASE].y
    thumb_up = thumb_tip_y < thumb_ip_y < thumb_mcp_y < thumb_base_y

    index_wrapped = (
    hand_landmarks.landmark[INDEX_TIP].y >
    hand_landmarks.landmark[INDEX_PIP].y >
    hand_landmarks.landmark[INDEX_BASE].y
    )

    middle_wrapped = (
        hand_landmarks.landmark[MIDDLE_TIP].y >
        hand_landmarks.landmark[MIDDLE_PIP].y >
        hand_landmarks.landmark[MIDDLE_BASE].y
    )

    ring_wrapped = (
        hand_landmarks.landmark[RING_TIP].y >
        hand_landmarks.landmark[RING_PIP].y >
        hand_landmarks.landmark[RING_BASE].y
    )

    pinky_wrapped = (
        hand_landmarks.landmark[PINKY_TIP].y >
        hand_landmarks.landmark[PINKY_PIP].y >
        hand_landmarks.landmark[PINKY_BASE].y
    )
    
    if index_wrapped and middle_wrapped and ring_wrapped and pinky_wrapped:
        if thumb_up:
            print("Thumbs up detected: triggering volume up")
            return True
        elif thumb_tip_y > thumb_ip_y > thumb_mcp_y > thumb_base_y:
            print("Thumbs down detected: triggering volume down")
            return True
    return False

# SKIP / REWIND
def is_finger_pointing(hand_landmarks):
    # Check if the index finger is pointing up and the rest are down
    
    
    return False