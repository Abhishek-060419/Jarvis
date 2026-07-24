import sounddevice as sd
import soundfile as sf
from pathlib import Path
import numpy as np
import time

SAMPLE_RATE = 48000
CHANNELS = 1

THRESHOLD = 0.008
SILENCE_LIMIT = 200

WAIT_FOR_SPEECH_TIMEOUT = 15
MAX_SPEECH_DURATION = 60

OUTPUT_PATH = (
    Path(__file__).resolve().parent.parent
    / "audio"
    / "recording.wav"
)

audio_chunks = []
silence_count = 0
speech_detected = False


def process_audio(indata, frames, time_info, status):
    global silence_count, speech_detected

    if status:
        print(status)

    volume = np.mean(np.abs(indata))

    # Detect beginning of speech
    if volume > THRESHOLD:
        speech_detected = True
        silence_count = 0

    # Store audio only after speech has started
    if speech_detected:
        audio_chunks.append(indata.copy())

        # Count silence only after speech has started
        if volume <= THRESHOLD:
            silence_count += 1


def listen():
    global silence_count, speech_detected

    audio_chunks.clear()
    silence_count = 0
    speech_detected = False

    waiting_start = time.time()
    speech_start = None

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        callback=process_audio,
    ):

        while True:

            # Waiting for user to start speaking
            if not speech_detected:

                if time.time() - waiting_start > WAIT_FOR_SPEECH_TIMEOUT:
                    print("No speech detected.")
                    break

            else:

                # Start speech timer once
                if speech_start is None:
                    speech_start = time.time()

                # Stop after prolonged silence
                if silence_count >= SILENCE_LIMIT:
                    print("Speech finished.")
                    break

                # Safety limit for very long recordings
                if time.time() - speech_start > MAX_SPEECH_DURATION:
                    print("Maximum speech duration reached.")
                    break

            time.sleep(0.01)

    if not audio_chunks:
        return None

    audio = np.concatenate(audio_chunks, axis=0)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    sf.write(OUTPUT_PATH, audio, SAMPLE_RATE)

    return str(OUTPUT_PATH)


