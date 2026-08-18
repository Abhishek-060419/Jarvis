from pathlib import Path
from piper.voice import PiperVoice #text-to-speech engine/model interface (a class used to load the voice model)
import wave #used to create wav files 
import winsound #used for audio playback
from piper.config import SynthesisConfig #used to control features of the voice

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "piper"
    / "en_GB-alan-medium.onnx"
)

Output_path=(
    Path(__file__).resolve().parent.parent/"audio"/"speachtts.wav")


config=SynthesisConfig(length_scale=0.8)

VOICE=PiperVoice.load(MODEL_PATH)

def speak(text:str):
    with wave.open(str(Output_path),"wb") as wav_file:
        VOICE.synthesize_wav(text,wav_file,syn_config=config)

    winsound.PlaySound(str(Output_path),winsound.SND_FILENAME)