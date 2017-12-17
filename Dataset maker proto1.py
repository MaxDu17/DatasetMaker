import pyaudio
import sys
import wave


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

recorder = pyaudio.PyAudio()

stream = recorder.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("I'm recording")

frames = []

for i in range(0, int((RATE/CHUNK)*RECORD_SECONDS)): #this iterates it up to the chunks needed in seconds
    data = stream.read(CHUNK)
    frames.append(data)


print("done")

stream.stop_stream()
stream.close()
recorder.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(recorder.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()
