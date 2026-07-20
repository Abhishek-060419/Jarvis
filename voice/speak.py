from pathlib import Path
from piper.voice import PiperVoice

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "piper"
    / "en_GB-alan-medium.onnx"
)

VOICE=PiperVoice.load(MODEL_PATH)