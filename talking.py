
import pyttsx3
import speech_recognition as sr


listener = sr.Recognizer()  # object creation for listening
engine = pyttsx3.init()  # object creation for text to speech

engine.setProperty('rate', 125)  # rate of speaking
voices = engine.getProperty('voices')
# 1 for female voice and 0 for male voice
engine.setProperty('voice', voices[1].id)

# my device index is 1, you have to put your device index
my_mic = sr.Microphone(device_index=1)



def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("A child who reads can have a stronger self-confidence. "
     "This child can face situations nicely. Reading good books creates ethical, moral values in a child. "
     "They get to know about society, culture, political conditions, etc. They know about the culture and lifestyle of different "
     "people from all over the world. At this age group, they feel mixed emotions that need to be expressed to their mental wellness. "
     "When a child reads a book, she empathizes with the characters of the book. In this way, they achieve their emotional intelligence and learn how to react in different situations.")
