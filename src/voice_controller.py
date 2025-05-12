# Handles voice recognition

import speech_recognition as sr

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
            if "pause" in command:
                print("Pausing...")
                # Trigger pause action here
            elif "faster" in command:
                print("Speeding up...")
                # Trigger speed up action here
            elif "slower" in command:
                print("Slowing down...")
                # Trigger slow down action here
            elif "play" in command:
                print("Playing...")
                # Trigger play action here
            elif "skip" in command:
                print("Skipping...")
                # Trigger skip action here
            elif "rewind" in command:
                print("Rewinding...")
                # Trigger rewind action here
            elif "volume up" in command:
                print("Volume up...")
                # Trigger volume up action here
            elif "volume down" in command:
                print("Volume down...")
                # Trigger volume down action here

    except Exception as e:
        print(f"Could not request results; {e}")

