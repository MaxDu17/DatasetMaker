import pyaudio
import sys
import wave
import keyboard
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 4096
RECORD_SECONDS = 2

inhaleCounter = 0
exhaleCounter = 0
unknownCounter = 0
Time = time.clock()
life = True


def fileName(curr_number,status):
    if status == 0:
        result = "dataSPLIT/inhale/" +str(curr_number) + ".wav"
    elif status ==1:
        result = "dataSPLIT/exhale/" +str(curr_number) + ".wav"
    else:
        result = "dataSPLIT/unknown/" + str(curr_number) + ".wav"
    return result
    
def makeFile(stream, recorder,file_name,frames):
    stream.stop_stream()
    stream.close()
    recorder.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(recorder.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()


def record():
    global inhaleCounter
    global exhaleCounter
    global unknownCounter
    global life
    Time = time.clock()
    recorder = pyaudio.PyAudio()
    stream = recorder.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    
    frames = []
    while Time + RECORD_SECONDS > time.clock():
        data = stream.read(CHUNK)
        frames.append(data)
    type = input("type? (I,O,U,X,Q)\n")
    if type == 'i':
        file_name = fileName(inhaleCounter, 0)
        inhaleCounter += 1
        makeFile(stream,recorder,file_name,frames)

    elif type == 'o':
        file_name = fileName(exhaleCounter,1)
        exhaleCounter += 1
        makeFile(stream, recorder,file_name,frames)
    elif type == 'u':
        file_name = fileName(unknownCounter, 2)
        unknownCounter += 1
        makeFile(stream, recorder, file_name, frames)
    elif type == 'q':
        life = False

    else:
        print('discarded')




if __name__ == '__main__':
    inhaleCounter = int(input("what inhale?\n"))
    exhaleCounter = int(input("what exhale?\n"))
    unknownCounter = int(input("what unknown?\n"))
    print("starting in 3")
    time.sleep(1)
    print("starting in 2")
    time.sleep(1)
    print("starting in 1")
    time.sleep(1)
    print("live")
    while True:
        if life:
            record()
            time.sleep(0.1)
        else:
            break
        
