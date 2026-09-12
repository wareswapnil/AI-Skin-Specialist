# Step1: Record audio from microphone

# dependencies: ffmpeg, portaudio, pyaudio (commands available in description)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
print("GROQ KEY =", os.getenv("GROQ_API_KEY"))

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        logging.info("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        logging.info("Start speaking now...")
        
        # Record the audio
        audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        logging.info("Recording complete.")
        
        # Convert the recorded audio to an MP3 file
        wav_data = audio_data.get_wav_data()
        audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
        audio_segment.export(file_path, format="mp3", bitrate="128k")
        
        logging.info(f"Audio saved to {file_path}")

audio_filepath="patient_voice_test.mp3"
#record_audio(audio_filepath, timeout=20, phrase_time_limit=10)


# Step2: Convert audio to text
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def transcribe_patient_voice(audio_filepath):
    groq_api_key = os.environ.get("GROQ_API_KEY")

    client = Groq(api_key=groq_api_key)
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=os.environ.get("WHISPER_MODEL", "whisper-large-v3"),
        )

    return transcription.text
import os
from io import BytesIO

import speech_recognition as sr
from pydub import AudioSegment
from groq import Groq
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Record audio from microphone and save as MP3.
    """

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        logging.info("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        logging.info("Start speaking now...")

        audio_data = recognizer.listen(
            source,
            timeout=timeout,
            phrase_time_limit=phrase_time_limit
        )

        logging.info("Recording complete.")

        wav_data = audio_data.get_wav_data()
        audio_segment = AudioSegment.from_wav(BytesIO(wav_data))

        audio_segment.export(
            file_path,
            format="mp3",
            bitrate="128k"
        )

        logging.info(f"Audio saved to {file_path}")


def transcribe_patient_voice(audio_filepath):
    """
    Convert speech audio to text using Groq Whisper.
    """

    groq_api_key = os.getenv("GROQ_API_KEY")
 
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    client = Groq(api_key=groq_api_key)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3"
        )

    return transcription.text


# Test section
if __name__ == "__main__":
    audio_file = r"C:\Users\wares\Downloads\ai-skin-specialist\ai-skin-specialist-main\patient_voice_test.mp3"

    if os.path.exists(audio_file):
        text = transcribe_patient_voice(audio_file)
        print("\nTranscription:")
        print(text)
    else:
        print(f"File not found: {audio_file}")