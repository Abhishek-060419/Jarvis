from voice.listen import listen
from brain.transcribe import transcribe
from brain.parser import parse
from brain.dispatcher import dispatch_actions
from voice.speak import speak
from actions.verifier import verify

speak("Welcome back, boss. All systems operational. How may I assist you today?")
while True:
    audio_path = listen()

    if audio_path is None:
        continue

    print("🧠 Transcribing...")
    text = transcribe(audio_path)

    print(f"\n📝 Recognized Text:\n{text}")

    print("\n🧩 Parsing...")
    command = parse(text)

    print(command)

    verified=verify(text,command["intent"],command["parameter"])

    print(verified)

    if not verified:
        continue

    should_continue = dispatch_actions(verified["actions"])

    if not should_continue:
        break

print("Jarvis terminated.")