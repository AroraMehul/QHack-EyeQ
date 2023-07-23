"""
Script to convert text to speech
"""
import pyttsx3

def text_to_speech(text):
    """
    Function for text to speech output
    """
    engine = pyttsx3.init() # object creation
    engine.setProperty('rate', 125)     # setting up new voice rate
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()
    engine.stop()
