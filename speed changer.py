import pyaudio
import sys
import wave
import keyboard
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

inhaleCounter = 0
exhaleCounter = 0
life = True


def makefileName(curr_number, inhale):
    if inhale:
        result = "datatest/inhale_125" + str(curr_number) + ".wav"
    else:
        result = "datatest/exhale_125" + str(curr_number) + ".wav"
    return result


def modify():
    makefileName()

if __name__ == '__main__':
    print("starting session, press 1 to inhale, 2 to exhale")
    modify()
        
