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


def fileName(curr_number):

    result = "sen_data/unknown/" + str(curr_number) + ".wav"
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
    global unknownCounter
    global life
    file_name = ""
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
    print("done")
    file_name = fileName(unknownCounter)
    unknownCounter += 1
    makeFile(stream,recorder,file_name,frames)

def make_blanks():
    global unknownCounter
    frames = []
    for i in range(8192):
        frames.append(bytes(0))
    file_name = ""
    Time = time.clock()
    recorder = pyaudio.PyAudio()
    stream = recorder.open(format=FORMAT,
                           channels=CHANNELS,
                           rate=RATE,
                           input=True,
                           frames_per_buffer=CHUNK)

    file_name = fileName(unknownCounter)
    unknownCounter += 1
    makeFile(stream, recorder, file_name, frames)
    print("done")

if __name__ == '__main__':
    unknownCounter = int(input("what unknown?\n"))
    print("starting in 3")
    time.sleep(1)
    print("starting in 2")
    time.sleep(1)
    print("starting in 1")
    time.sleep(1)
    print("live")
    for i in range(200):
        if life:
            record()
            time.sleep(0.1)

        else:
            break
        print(unknownCounter)
