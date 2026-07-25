from voice.listen import listen
from brain.transcribe import transcribe
audio_path = listen()


if audio_path is None:
    print("No audio captured.")
    exit()
print("🧠 Transcribing...")
text = transcribe(audio_path)

print(f"\n📝 Recognized Text:\n{text}")