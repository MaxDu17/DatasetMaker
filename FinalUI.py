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
Time = time.clock()
life = True


def fileName(curr_number,inhale):
    if inhale:
        result = "datatest/inhale_" +str(curr_number) + ".wav"
    else:
        result = "datatest/exhale_" +str(curr_number) + ".wav"
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
    global life
    Time = time.clock()
    recorder = pyaudio.PyAudio()
    stream = recorder.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    
    frames = []
    while Time + 5 > time.clock():
        data = stream.read(CHUNK)
        frames.append(data)
    type = input("type? (I,O,X,Q)\n")
    if type == 'i':
        file_name = fileName(inhaleCounter, True)
        inhaleCounter += 1
        makeFile(stream,recorder,file_name,frames)

    elif type == 'o':
        file_name = fileName(exhaleCounter, False)
        exhaleCounter += 1
        makeFile(stream, recorder,file_name,frames)

    elif type == 'q':
        life = False

    else:
        print('discarded')




if __name__ == '__main__':
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
        
