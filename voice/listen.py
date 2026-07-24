import sounddevice as sd
import soundfile as sf
from pathlib import Path
import numpy as np 
import time

SAMPLE_RATE=48000
CHANNELS=1
THRESHOLD=0.008
SILENCE_LIMIT=200
MAX_RECORDING_TIME=15

OUTPUT_PATH=(Path(__file__).resolve().parent.parent/"audio"/"recording.wav")


audio_chunks=[]
silence_count=0
speech_detected = False

def process_audio(indata, frames, time, status):

    if status:
        print(status)

    global silence_count,speech_detected

    audio_chunks.append(indata.copy())
    volume=np.mean(np.abs(indata))
    if volume>THRESHOLD:
        speech_detected=True
        silence_count=0
    elif speech_detected:
        silence_count+=1

def listen():
    #print("Recording... Speak now!")
    #audio=sd.rec(frames=FRAMES,samplerate=SAMPLE_RATE,channels=CHANNELS,dtype="float32")

    #sd.wait()

    audio_chunks.clear()

    global silence_count,speech_detected   
    silence_count=0
    speech_detected = False

    start_time=time.time()

    with sd.InputStream(samplerate=SAMPLE_RATE,channels=CHANNELS,callback=process_audio):

        while silence_count<SILENCE_LIMIT:
            if time.time() - start_time > MAX_RECORDING_TIME:
                print("Maximum recording time reached.")
                break

            time.sleep(0.01)

    if not audio_chunks:
        return None
    
    audio=np.concatenate(audio_chunks)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    sf.write(OUTPUT_PATH,audio,SAMPLE_RATE)

    return str(OUTPUT_PATH)


