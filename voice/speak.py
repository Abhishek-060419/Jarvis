from pathlib import Path
from piper.voice import PiperVoice
import wave
import winsound
from piper.config import SynthesisConfig

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "piper"
    / "en_GB-alan-medium.onnx"
)

config=SynthesisConfig(length_scale=0.8)

VOICE=PiperVoice.load(MODEL_PATH)

def speak(text:str):
    with wave.open("output.wav","wb") as wav_file:
        VOICE.synthesize_wav(text,wav_file,syn_config=config)

    winsound.PlaySound("output.wav",winsound.SND_FILENAME)