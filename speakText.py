import pyttsx3

engine = pyttsx3.init()
engine.setProperty('volume', '1.0')

def speak(tell):
    engine.say(tell)
    engine.runAndWait()