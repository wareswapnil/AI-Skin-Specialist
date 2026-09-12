import subprocess
import platform
import os
from gtts import gTTS


def text_to_speech_with_gtts(
    input_text,
    output_filepath="doctor_response.mp3"
):
    language = "en"

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )

    audioobj.save(output_filepath)

    os_name = platform.system()

    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(["afplay", output_filepath])

        elif os_name == "Windows":  # Windows
            os.startfile(output_filepath)

        elif os_name == "Linux":  # Linux
            subprocess.run(["xdg-open", output_filepath])

        else:
            raise OSError("Unsupported operating system")

    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

    return output_filepath


if __name__ == "__main__":
    input_text = (
        "Hello, this is a test of the text to speech functionality. "
        "My name is AI with Swapnil Ware."
    )

    output_filepath = "output_gtts.mp3"

    text_to_speech_with_gtts(
        input_text,
        output_filepath
    )