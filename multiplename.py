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



def fileName(curr_number,inhale):
    if inhale:
        result = "datatest/inhale" +str(curr_number) + ".wav"
    else:
        result = "datatest/exhale" +str(curr_number) + ".wav"
    return result
    


def record():
    global inhaleCounter
    global exhaleCounter
    global life
    recorder = pyaudio.PyAudio()
    stream = recorder.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    
    frames = []
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('1'):
            file_name = fileName(inhaleCounter,True)
            inhaleCounter += 1
            break
        if keyboard.is_pressed('2'):
            file_name = fileName(exhaleCounter, False)
            exhaleCounter += 1
            break
        if keyboard.is_pressed('q'):
            life = False
            file_name = "data/DELETE ME.wav"
            break


    print("done")
    
    stream.stop_stream()
    stream.close()
    recorder.terminate()
    
    wf = wave.open(file_name, 'wb')
    
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(recorder.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

if __name__ == '__main__':
    print("starting session, press 1 to inhale, 2 to exhale")
    while True:
        if life:
            record()
            time.sleep(0.1)
        else:
            break
        
