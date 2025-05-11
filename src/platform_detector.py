import pygetwindow as gw

def get_platform():
    active_window = gw.getActiveWindow()

    if active_window:
        if "Lecture Recordings" in active_window.title:
            return "Brightspace"
        elif "Youtube" in active_window.title:
            return "Youtube"
    return "unknown"