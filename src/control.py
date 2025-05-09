# Triggers keyboard and mouse events

import pyautogui

def pause_play():
    pyautogui.press('space')

def skip_forward():
    pyautogui.press('right')

def skip_backward():
    pyautogui.press('left')