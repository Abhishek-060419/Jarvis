from voice.listen import listen

print("Recording... Speak naturally.")
audio_path = listen()

if audio_path:
    print(f"\nRecording saved to:\n{audio_path}")
    print("Open the WAV file and listen to it.")
else:
    print("No recording was captured.")