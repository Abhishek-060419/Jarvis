from voice.listen import listen
from brain.transcribe import transcribe
from brain.parser import parse

audio_path = listen()

if audio_path is None:
    exit()

print("🧠 Transcribing...")
text = transcribe(audio_path)

print(f"\n📝 Recognized Text:\n{text}")

print("\n🧩 Parsing...")
command = parse(text)

print(command)