import time
import speech_recognition as sr
import mac_say

# start bg listening
# list of cmds
# list of trigger words
# list of actions
# run in while loop
# add keyboard interactions to start/stop


# start bg listening
# cmd - execute
    # listen for new set of commands
    # get obj
# listen again

trigger_word = "Hello world"

# system asks "how can i help?"

primary_cmds = ['Remember this',
                'Take me ',
                'Read this',
                'Look for an object',
                'Describe the surrouding']
secondary = False
# secondary_cmd = ['mobile']

def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    global secondary
    try:
        text = recognizer.recognize_google(audio)
        if text in primary_cmds and not secondary:
            secondary = True
            # action
            if text == primary_cmds[0]:
                mac_say.say(text)
                print(text)
                # register new object
            elif text == primary_cmds[1]:
                mac_say.say(text)
                print(text)
                # nav to old obj
            elif text == primary_cmds[2]:
                mac_say.say(text)
                print(text)
                # trigger OCR
            elif text == primary_cmds[3]:
                mac_say.say(text)
                print(text)
                # run imgnet on captured frame
            elif text == primary_cmds[4]:
                # run img captioning model
                mac_say.say(text)
                print(text)

        elif secondary:
            object_name = text
            secondary = False
            print(object_name)
        elif text not in primary_cmds and not secondary:
            print('other')
        # print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

while True:
    continue