"""
Script to control interation with the user
"""

import time
import speech_recognition as sr
import pyttsx3
from navigation.occupancy_planning import plan
from navigation.occupancy_planning import get_current_coord, save_coord

def speak(audio):
    """
    Text to Speech output
    """
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """
    Takes user voice command
    """
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en')
        print(f"User said: {query}\n")

    except Exception as error:
        print(error)
        print("Unable to Recognize your voice.")
        return "None"

    return query

primary_cmds = ['Remember this',
                'Take me to my item',
                'Read this',
                'Look for an object',
                'Describe the surrouding']

if __name__ == '__main__':
    engine = pyttsx3.init() # object creation
    engine.setProperty('rate', 125)     # setting up new voice rate
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    while True:
        # Event loop
        query = takeCommand().lower()
        if "eyeQ" in query or 'hello' in query:
            speak("How may i help you?")

        elif 'navigation' in query or 'start' in query:
            speak("Starting camera and mapping")

        elif "remember" in query or 'object' in query:
            speak("please name this object")
            obj_name = takeCommand()
            curr_coord = get_current_coord()
            save_coord(curr_coord)
            speak(f'{obj_name} is saved at this location')

        elif 'where is' in query or 'look for':
            query = query.replace('where is', '')
            query = query.replace('look for', '')
            speak(f"Looking for {query}")
            # table
            
            time.sleep(1)
            speak(f"Found {query} about one meters straight and slight right from your current location")

        elif "read" in query:
            speak("reading")
            # runOCRScript
            text = 'Manchester United is a shitty football team'
            speak(text)
        elif "look for" in query:
            # runImagenetmodel
            # chair
            query = query.replace('look for', '')
            speak(f'Looking for {query}')
            time.sleep(2)
            speak(f"found {query}, one point five meters straight and slight left from your current location")

        elif 'surrounding' in query:
            # run img captioning model
            speak('In front of you, there is a pervert sitting with Mehul Arora')
        # elif "camera" in query or "take a photo" in query:
        # 	ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif 'take me' in query:
            query = query.replace('take me to','')
            speak(f'Fetching location of {query}')
            time.sleep(1)
            speak(f'Generating path to {query}. Please wait')
            time.sleep(3)
            speak(f'Starting navigation to {query}. Go Straight for 3.5 meters.')
            time.sleep(1.5)
            speak('go straight')
            time.sleep(1)
            speak('turn left')
            time.sleep(2)
            speak('go straight')
            time.sleep(2)
            speak(f'you have arrived. {query} is on the left')
            



        elif "what is" in query or "who is" in query:
            
            # Use the same API key
            # that we have generated earlier
            # client = wolframalpha.Client("API_ID")
            # res = client.query(query)
            pass
            # try:
            # 	print (next(res.results).text)
            # 	speak (next(res.results).text)
            # except StopIteration:
            # 	print ("No results")

        # elif "" in query:
            # Command go here
            # For adding more commands
