import pygetwindow as gw

def get_platform():
    active_window = gw.getActiveWindow()

    if active_window:
        if "Lecture Recordings" in active_window.title:
            return "Brightspace"
        elif "YouTube" in active_window.title:
            return "Youtube"
        elif "Netflix" in active_window.title:
            return "Netflix"
    return "unknown"