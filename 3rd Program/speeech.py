# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:48:54 2018

@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:39:18 2018

@author: Lenovo
"""

import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True
def say(text):
    subprocess.call('say'+text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
             format = pa.get_format_from_width(wf.getsampwidth()),
             channels = wf.getnchannels(),
             rate = wf.getframerate(),
             output = True)
    data_stream = wf.readframes(chunk)
     
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
     
    stream.close()
    pa.terminate()
     
#play_audio('./pedantic.wav')
r = sr.Recognizer()
cmd = Commander()
def initSpeech():
    print("Listening..")
    play_audio('./pedantic.wav')
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
        
    play_audio('./job-done.wav')
    command = ""
    try:
        command = r.recognize_google(audio) 
        f = open("required.doc",'w')
        f.write(command)
        f.close()
        
    except:
        print("Couldn't understand you, Dude!")
    print("Your command is:",command)
    say("You said: "+ command)
#while running == True:
#    initSpeech()
    
initSpeech()


    
     
