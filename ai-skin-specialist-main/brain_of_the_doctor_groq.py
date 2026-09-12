import base64
import os
from io import BytesIO

from dotenv import load_dotenv
from groq import Groq
from PIL import Image


load_dotenv()


def encode_image_for_groq(filepath):
    image = Image.open(filepath)
    image.thumbnail((1024, 1024))

    buffer = BytesIO()
    image.convert("RGB").save(buffer, format="JPEG", quality=75)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def brain_of_the_doctor(patient_text, image_filepath=None, video_filepath=None):
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Missing GROQ_API_KEY in .env or environment")

    if not image_filepath:
        raise ValueError("Groq vision requires an image. Please upload a skin image.")

    # Groq vision does not accept video here. When main.py passes both image and
    # video, this uses the same image as the visual input and ignores the video.
    image_data = encode_image_for_groq(image_filepath)

    prompt = (
        "You are a confident, natural doctor specializing in skin care. Speak with the reassurance, clarity, and authority of a real doctor. "
        "Limit your entire response to two or three sentences maximum. "
        "If the patient has provided a video, explain that you are reviewing the uploaded image because this model cannot process video directly. "
        "Do not use any special characters, symbols, asterisks, or markdown formatting in your response because it will be converted directly to audio.\n\n"
        f"Patient text: {patient_text}"
    )

    if video_filepath:
        prompt += "\nThe patient also uploaded a video, but use the provided image as the visual reference."

    client = Groq(api_key=groq_api_key)
    response = client.chat.completions.create(
        model=os.environ.get("GROQ_MODEL", "qwen/qwen3.6-27b"),
       
        max_completion_tokens=1000,
        messages=[
            {
                "role": "system",
                "content": "You are a careful skin care assistant. Give general information, not a diagnosis.",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}",
                        },
                    },
                ],
            },
        ],
    )

    return response.choices[0].message.content


# OLD CODE KEPT FOR REFERENCE
# import base64
# import os
# from io import BytesIO
#
# from dotenv import load_dotenv
# from groq import Groq
# from PIL import Image
#
#
# folder = os.path.dirname(__file__)
# env_path = os.path.join(folder, ".env")
# load_dotenv(env_path)
#
# api_key = os.environ.get("GROQ_API_KEY")
# if not api_key:
#     raise ValueError("Missing GROQ_API_KEY in .env or environment")
#
#
# image_path = os.path.join(folder, "sample-image.png")
#
# image = Image.open(image_path)
# image.thumbnail((1024, 1024))
#
# buffer = BytesIO()
# image.convert("RGB").save(buffer, format="JPEG", quality=75)
# image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
#
# client = Groq(api_key=api_key)
#
# response = client.chat.completions.create(
#     model=os.environ.get("GROQ_MODEL", "meta-llama/llama-4-scout-17b-16e-instruct"),
#     max_completion_tokens=1000,
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful medical assistant. Give general information, not a diagnosis.",
#         },
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "What do you see in this image? Give general skin care advice, not a diagnosis.",
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{image_data}",
#                     },
#                 },
#             ],
#         },
#     ],
# )
#
# print(response.choices[0].message.content)
