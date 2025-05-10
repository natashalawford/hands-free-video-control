# Triggers keyboard and mouse events

import pyautogui

def pause_play():
    pyautogui.press('space')

def skip_forward():
    pyautogui.press('right')

def skip_backward():
    pyautogui.press('left')

def speed_up():
    pyautogui.press('+')

def slow_down():
    pyautogui.press('_')

def volume_up():
    pyautogui.press('up')

def volume_down():
    pyautogui.press('down')