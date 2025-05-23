import speech_recognition as sr
import pyttsx3
import pyaudio

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results. Check your internet connection.")
            return ""

def control_appliance(command):
    if "turn on the light" in command:
        speak("Turning on the light.")
        # Simulated action
        print("💡 Light is ON")
    elif "turn off the light" in command:
        speak("Turning off the light.")
        print("💡 Light is OFF")
    else:
        speak("Command not recognized.")

# Main loop
if __name__ == "__main__":
    speak("Voice control system activated.")
    while True:
        cmd = listen_command()
        if "exit" in cmd or "stop" in cmd:
            speak("Shutting down. Goodbye!")
            break
        control_appliance(cmd)