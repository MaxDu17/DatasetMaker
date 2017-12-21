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






def fileName(curr_number):
    result = "demo" +str(curr_number) + ".wav"
    return result
    


def record(file_name):
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
        if keyboard.is_pressed('d'):
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
    print("starting session, press i to inhale, o to exhale")
    for i in range(8): 
        result = fileName(i)
        record(result)
        time.sleep(0.1)
