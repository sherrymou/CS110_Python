'''
Keni Mou
Kmou1@binghamton.edu
Kristy Stevens
ksteven4@binghamton.edu
Final Project 5/7
Lab Section 52
CA Kyle Mille
'''

#This file is written by Kristy

'''
Notes:
this is the ending sound
it will be played after counting down is over
'''

import pyaudio  
import wave  
import sys


def playAudio():
    chunk = 1024  

    ring = wave.open(r"Msg.wav","rb")  

    p = pyaudio.PyAudio()  

    stream = p.open(format = p.get_format_from_width(ring.getsampwidth()),  
                    channels = ring.getnchannels(),  
                    rate = ring.getframerate(),  
                    output = True)  

    data = ring.readframes(chunk)  
      
    while data != '':  
        stream.write(data)  
        data = ring.readframes(chunk)  

    stream.stop_stream()  
    stream.close()  
      
    p.terminate()  
