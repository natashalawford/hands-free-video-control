# Triggers keyboard and mouse events

import pyautogui
from platform_detector import get_platform

def pause_play():
    pyautogui.press('space')

def skip_forward():
    pyautogui.press('right')

def skip_backward():
    pyautogui.press('left')

def speed_up():
    if get_platform() == "Brightspace":
        pyautogui.press('+')
    elif get_platform() == "Youtube" or get_platform() == "Netflix":
        pyautogui.press('>')

def slow_down():
    if get_platform() == "Brightspace":
        pyautogui.press('_')
    elif get_platform() == "Youtube" or get_platform() == "Netflix":
        pyautogui.press('<')

def volume_up():
    pyautogui.press('up')

def volume_down():
    pyautogui.press('down')