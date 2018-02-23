import pyaudio
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
        result = "dataSPLIT/inhale/" + str(curr_number)+"_x" + ".wav"
    elif status == 1:
        result = "dataSPLIT/exhale/" + str(curr_number) +"x"+ ".wav"
    else:
        result = "dataSPLIT/unknown/" + str(curr_number)+ "x" + ".wav"
    return result

def makereadfileName(curr_number,status):
    if status == 0:
        result = "dataSPLIT/inhale/" + str(curr_number) + ".wav"
    elif status == 1:
        result = "dataSPLIT/exhale/" + str(curr_number) + ".wav"
    else:
        result = "dataSPLIT/unknown/" + str(curr_number) + ".wav"
    return result
def modify(curr_number,status):
    distort = random.random()
    distort +=0.5
    file_name = makefileName(curr_number,status)
    openfile_name = makereadfileName(curr_number,status)
    wf = wave.open(openfile_name, 'rb')
    frames = []
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                input = True,
                frames_per_buffer=CHUNK)

    data = wf.readframes(CHUNK)

    while len(data) > 0:
        data = wf.readframes(CHUNK)
        stream.write(data)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

    tbw = wave.open(file_name, 'wb')

    tbw.setnchannels(CHANNELS)
    tbw.setsampwidth(p.get_sample_size(FORMAT))
    tbw.setframerate(RATE/distort)
    tbw.writeframes(b"".join(frames))
    tbw.close()


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

        
