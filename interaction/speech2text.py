

# add background listening

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
with mic as source:
    r.adjust_for_ambient_noise(source)
    # use Snowbow ai for hotword detection in background audio
    audio = r.listen(source)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=5)
text = r.recognize_google(audio)
    # text = r.recognize_sphinx(audio)
print(text)

# with sr.Microphone() as source:
#     r = sr.Recognizer()
#     # read the audio data from the default microphone
#     audio_data = source.record(source, duration=5)
#     print("Recognizing...")
#     # convert speech to text
#     text = r.recognize_google(audio_data)
#     print(text)