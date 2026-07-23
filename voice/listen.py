import sounddevice as sd
import soundfile as sf
from pathlib import Path
import numpy as np 
import time

SAMPLE_RATE=48000
RECORD_TIME=4
CHANNELS=1
FRAMES=SAMPLE_RATE*RECORD_TIME
THRESHOLD=0.015
SILENCE_LIMIT=15

OUTPUT_PATH=(Path(__file__).resolve().parent.parent/"audio"/"recording.wav")

audio_chunks=[]
silence_count=0

def process_audio(indata, frames, time, status):
    global silence_count
    audio_chunks.append(indata.copy())
    volume=np.mean(np.abs(indata))
    if volume<THRESHOLD:
        silence_count+=1
    else:
        silence_count=0

def listen():
    #print("Recording... Speak now!")
    #audio=sd.rec(frames=FRAMES,samplerate=SAMPLE_RATE,channels=CHANNELS,dtype="float32")

    #sd.wait()

    audio_chunks.clear()
    global silence_count    
    silence_count=0

    with sd.InputStream(samplerate=SAMPLE_RATE,channels=CHANNELS,callback=process_audio):

        while silence_count<SILENCE_LIMIT:
            time.sleep(0.01)

    if not audio_chunks:
        return None
    
    audio=np.concatenate(audio_chunks)

    sf.write(OUTPUT_PATH,audio,SAMPLE_RATE)

    return str(OUTPUT_PATH)


