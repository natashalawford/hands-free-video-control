# Handles voice recognition

import speech_recognition as sr
from control import pause_play, skip_backward, skip_forward, speed_up, slow_down,\
    volume_up, volume_down

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            # Recognize speech using Google Web Speech API
            command = r.recognize_google(audio)
            print(f"Command: {command}")
            command = command.lower()

            # Check for specific commands and trigger actions
            if "pause" in command or "play" in command:
                print("Pausing/Playing...")
                pause_play()
            elif "faster" in command:
                print("Speeding up...")
                speed_up()
            elif "slower" in command:
                print("Slowing down...")
                slow_down()
            elif "skip" in command:
                print("Skipping...")
                skip_forward()
            elif "rewind" in command:
                print("Rewinding...")
                skip_backward()
            elif "volume up" in command:
                print("Volume up...")
                volume_up()
            elif "volume down" in command:
                print("Volume down...")
                volume_down()

    except Exception as e:
        print(f"Could not request results; {e}")

