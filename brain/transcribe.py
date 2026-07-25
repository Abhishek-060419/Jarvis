from faster_whisper import WhisperModel

model=WhisperModel("medium",device="cuda",compute_type="float16")

def transcribe(audio_path):
    segments, info=model.transcribe(audio_path)

    return " ".join(segment.text for segment in segments)


