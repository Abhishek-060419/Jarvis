from faster_whisper import WhisperModel

model=WhisperModel("small",device="cpu",compute_type="int8")

def transcribe(audio_path):
    segments, info=model.transcribe(audio_path)

    return " ".join(segment.text for segment in segments)


