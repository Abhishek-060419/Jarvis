import sounddevice as sd
import soundfile as sf
from pathlib import Path

SAMPLE_RATE=48000
RECORD_TIME=4
CHANNELS=1
FRAMES=SAMPLE_RATE*RECORD_TIME

Output_path=(Path(__file__).resolve().parent.parent/"audio"/"recording.wav")

def listen():
    print("Recording... Speak now!")
    audio=sd.rec(frames=FRAMES,samplerate=SAMPLE_RATE,channels=CHANNELS,dtype="float32")

    sd.wait()

    sf.write(Output_path,audio,SAMPLE_RATE)