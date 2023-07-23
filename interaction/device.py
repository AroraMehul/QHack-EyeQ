# import pyttsx3
import speech_recognition as sr
import datetime
import time
import mac_say


def speak(audio):
    mac_say.say(audio)
    # engine.say(audio)
    # engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

primary_cmds = ['Remember this',
                'Take me to my item',
                'Read this',
                'Look for an object',
                'Describe the surrouding']

# engine = pyttsx3.init('sapi5')
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


if __name__ == '__main__':
    while True:

        query = takeCommand().lower()

        if "remember" in query:
            speak("name this object")
            obj_name = takeCommand()
            speak(f'{obj_name} is saved at this location')

        elif 'where is' in query:
            query = query.replace('where is', '')
            speak(f"Looking for {query}")

        elif "read" in query:
            speak("reading")
            # runOCRScript
            text = 'Manchester United is a shitty football team'
            speak(text)
        elif "look for" in query:
            # runImagenetmodel
            query = query.replace('look for', '')
            speak(f'Looking for {query}')
        elif 'surrounding' in query:
            # run img captioning model
            speak('In front of you, there is a pervert sitting with Mehul Arora')
        # elif "camera" in query or "take a photo" in query:
        # 	ec.capture(0, "Jarvis Camera ", "img.jpg")
            
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
