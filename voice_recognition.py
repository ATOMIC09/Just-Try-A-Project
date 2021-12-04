import pyaudio
import speech_recognition as sr

# Select Mic
mic_list = sr.Microphone.list_microphone_names()
mic = sr.Microphone(1)

# Recognizer
recog = sr.Recognizer()

# Voice Input
with mic as source:
    while True:
        audio = recog.listen(source)
        try:
            print(recog.recognize_google(audio,language='th'))
        except:
            continue