from faster_whisper import WhisperModel  #speech recognition and stt model

model=WhisperModel("medium",device="cuda",compute_type="float16")

def transcribe(audio_path):
    segments, info=model.transcribe(audio_path,language="en")

    return " ".join(segment.text for segment in segments) #join the words with spaces " " in between them


