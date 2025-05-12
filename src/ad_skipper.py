import pyautogui
import threading
import time
import os

# Load the image of the skip ad button
skip_ad_fullscreen = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'skip_ad.png'))

# Specify where the button usually appears (bottom right-ish), might need to be adjusted
# depending on your screen size and layout

REGION = (1797, 1013, 698, 606)  # Adjust to your screen size/layout

def skip_ad_monitor():
    while True:
        try:
            # Look for the button image on the screen
            location = pyautogui.locateOnScreen(skip_ad_fullscreen, confidence=0.8, region=REGION)
            if location:
                print("🎯 Skip Ad button found, clicking...")
                pyautogui.click(pyautogui.center(location))
                time.sleep(1)  # Give it time to disappear
        except pyautogui.ImageNotFoundException:
            print("⏳ No ad to skip right now.")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)  # Check every 2 seconds


