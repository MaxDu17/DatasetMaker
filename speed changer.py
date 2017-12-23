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
        result = "datawork/inhale_125_" + str(curr_number) + ".wav"
    else:
        result = "datawork/exhale_125_" + str(curr_number) + ".wav"
    return result

def makereadfileName(curr_number,inhale):
    if inhale:
        result = "datawork/inhale" +str(curr_number) + ".wav"
    else:
        result = "datawork/exhale" +str(curr_number) + ".wav"
    return result
def modify(curr_number,inhale):
    file_name = makefileName(curr_number,inhale)
    openfile_name = makereadfileName(curr_number,inhale)
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
    tbw.setframerate(RATE/0.85)
    tbw.writeframes(b"".join(frames))
    tbw.close()


if __name__ == '__main__':
    print("reading")
    inhale = True
    for i in range(5):
        modify(i,inhale)
        inhale = not(inhale)
        modify(i, inhale)
        
