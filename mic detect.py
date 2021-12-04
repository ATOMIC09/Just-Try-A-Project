import pyaudio
import speech_recognition as sr

new_list = []
mic_list = sr.Microphone.list_microphone_names()
for i in range(len(mic_list)):
    new_list.append(mic_list[i] + '\n')
print(*new_list)