from voice.listen import listen
from brain.transcribe import transcribe
import os

print("=== JARVIS TEST ===")
print("Listening...\n")

audio_path = listen()

if audio_path is None:
    print("No recording was returned.")
    exit()

print("\nRecording completed.")
print(f"Audio Path: {audio_path}")

if not os.path.exists(audio_path):
    print("Error: Audio file was not found.")
    exit()

print("Audio file exists.")

print("\nTranscribing...")

try:
    text = transcribe(audio_path)

    print("\n========== RESULT ==========")
    print(f"Recognized Text: {text}")
    print("============================")

except Exception as e:
    print("\nTranscription failed!")
    print(type(e).__name__)
    print(e)