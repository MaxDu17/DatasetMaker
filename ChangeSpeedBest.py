import sys
import wave
import keyboard
import time
import random

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 4096
RECORD_SECONDS = 5

inhaleCounter = 0
exhaleCounter = 0
unknownCounter = 0
life = True


def makefileName(curr_number, status):
    if status == 0:
        result = "dataSPLITx/inhale/" + str(curr_number)+"_x" + ".wav"
    elif status == 1:
        result = "dataSPLITx/exhale/" + str(curr_number) +"x"+ ".wav"
    else:
        result = "dataSPLITx/unknown/" + str(curr_number)+ "x" + ".wav"
    return result

def makereadfileName(curr_number,status):
    if status == 0:
        result = "dataSPLITx/inhale/" + str(curr_number) + ".wav"
    elif status == 1:
        result = "dataSPLITx/exhale/" + str(curr_number) + ".wav"
    else:
        result = "dataSPLITx/unknown/" + str(curr_number) + ".wav"
    return result
def modify(curr_number,status):
    read_name = makereadfileName(curr_number,status)
    wave_object = wave.open(read_name,'r')
    #NOT FINISHED



if __name__ == '__main__':
    print("reading")
    status = 0
    for i in range(20):
        try:
            modify(inhaleCounter,0)
            inhaleCounter+=1
        except FileNotFoundError:
            print("end of inhales")
        try:
            modify(exhaleCounter,1)
            exhaleCounter+=1
        except FileNotFoundError:
            print("end of exhales")
        try:
            modify(unknownCounter,2)
            unknownCounter+=1
        except FileNotFoundError:
            print("end of unknowns")

        
