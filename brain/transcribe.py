from faster_whisper import WhisperModel

model=WhisperModel("small")

def transcribe(audio_path):
    segments, info=model.transcribe(audio_path)

    return " ".join(segment.text for segment in segments)


