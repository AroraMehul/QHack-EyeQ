import pyttsx3
import speech_recognition as sr
import datetime
import time

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
	
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query



# engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


if __name__ == '__main__':
	# This Function will clean any
	# command before execution of this python file

    while True:

        query = takeCommand().lower()

        if "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            # webbrowser.open("https://www.google.nl / maps / place/" + location + "")

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
