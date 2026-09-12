# Step1: Install and import dependencies
import anthropic
from dotenv import load_dotenv
import os
import base64
import mimetypes
# Step2: Create API keys & Client

load_dotenv()


def encode_file(filepath):
    with open(filepath, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


def get_media_type(filepath, fallback):
    media_type, _ = mimetypes.guess_type(filepath)
    return media_type or fallback


def brain_of_the_doctor(patient_text, image_filepath=None, video_filepath=None):

    minimax_api_key = os.environ.get("MINIMAX_API_KEY")

    prompt = (
    "You are a confident, natural doctor specializing in skin care. Speak with the reassurance, clarity, and authority of a real doctor. "
    "Limit your entire response to two or three sentences maximum. "
    "If the patient has not provided a video and only an image, your absolute priority is to ask them to provide a video first because mention that you need more details and you need a video showing the problem. "
    "Do not use any special characters, symbols, asterisks, or markdown formatting in your response because it will be converted directly to audio.\n\n"
    f"Patient text: {patient_text}"
)

    if video_filepath:
        media_content = {
            "type": "video",
            "source": {
                "type": "base64",
                "media_type": get_media_type(video_filepath, "video/mp4"),
                "data": encode_file(video_filepath),
            },
        }
    else:
        media_content = {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": get_media_type(image_filepath, "image/png"),
                "data": encode_file(image_filepath),
            },
        }

    client = anthropic.Anthropic(
        api_key=minimax_api_key,
        base_url=os.environ.get("MINIMAX_BASE_URL", "https://api.minimax.io/anthropic"),
    )
    response = client.messages.create(
        model=os.environ.get("MINIMAX_MODEL", "MiniMax-M3"),
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": [media_content, {"type": "text", "text": prompt}],
            }
        ],
    )

    doctors_response_in_text = response.content[0].text

    return doctors_response_in_text


"""api_key=os.environ.get("MINIMAX_API_KEY")
base_url="https://api.minimax.io/anthropic"

client = anthropic.Anthropic(api_key=api_key, base_url=base_url)

# Step3: Create message

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Hello, what can you help me with?",
            }
        ],
    }
]


# Image messages 
folder = os.path.dirname(__file__)
image_path = os.path.join(folder, "sample-image.png")


with open(image_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode("utf-8")
image_messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_data,
                },
            },
            {
                "type": "text",
                "text": "What do you see in this image?",
            },
        ],
    }
]

# Video Messages

video_path = os.path.join(folder, "test-video.mp4")
with open(video_path, "rb") as file:
    video_data = base64.b64encode(file.read()).decode("utf-8")

video_messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "source": {
                    "type": "base64",
                    "media_type": "video/mp4",
                    "data": video_data,
                },
            },
            {
                "type": "text",
                "text": "What is happening in this video?",
            },
        ],
    }
]


# Step4: Send Message

response = client.messages.create(
    model="MiniMax-M3",
    max_tokens=1000,
    messages=video_messages,
)



# Step5: Print Response

print(response.content[0].text)"""


