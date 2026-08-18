import sounddevice as sd
import soundfile as sf
from pathlib import Path
import numpy as np
import time
import winsound

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

def process_audio(indata #actual audio samples from microphone
                  ,frames #how many audio samples are contained in this indata
                  ,time_info #timestamps related to the audio stream
                  ,status #any warnings or errors
                  ):
    global silence_count, speech_detected

    if status:
        print(status)

    volume = np.mean(np.abs(indata))

    # Detect beginning of speech
    if volume > THRESHOLD:

        # This block should execute ONLY once
        if not speech_detected:
            speech_detected = True


        # Reset silence counter while speaking
        silence_count = 0

    # Store audio only after speech has started
    if speech_detected:
        audio_chunks.append(indata.copy()) #indata is reference to a buffer, so copy() creates a separate numpy array for the same

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

    print("🎙 Waiting for speech...")

    #sound device python library is used to record audio using our recording device(microphone) and play it using speakers
    with sd.InputStream(
        samplerate=SAMPLE_RATE,#how many times per second the microphone records sound samples
        channels=CHANNELS,#how many separate audio streams are being recorded
        callback=process_audio,
    ):
        print("\n🎤 Recording started...")
        winsound.Beep(1000, 150)
        
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

            time.sleep(0.01) #without a slight break, the loop would run as fast as the cpu, causing unnecessary checks and heavy load

    if not audio_chunks:
        return None

    audio = np.concatenate(audio_chunks, axis=0) #creates a single nummpy array with our full audio

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True) 
    sf.write(OUTPUT_PATH, audio, SAMPLE_RATE)  #soundfile library is used to read and write audio files

    return str(OUTPUT_PATH)


