# AI Skin Specialist

**AI Skin Specialist** is a Gradio-powered consultation assistant. A patient records a spoken description of their concern and uploads a skin image (or video), and the app returns a written and spoken doctor-style response.

Under the hood, it:

1. Transcribes the patient's voice using **Groq Whisper**
2. Sends the transcript and image to a **Groq vision model** for analysis
3. Converts the generated response into speech using **Deepgram text-to-speech**

> **⚠️ Disclaimer:** This project provides general informational guidance only. It is **not** a medical diagnosis and should never replace care from a licensed dermatologist or clinician. If you're experiencing severe symptoms, rapid spreading, fever, pain, bleeding, signs of infection, or any urgent concern, contact a licensed clinician immediately.

---

## Screenshots

**Main interface** — patient input (voice, image, video) alongside the doctor response panel:

![AI Skin Specialist main interface]  <img width="1522" height="720" alt="Screenshot 2026-09-13 005651" src="https://github.com/user-attachments/assets/ccc0d933-ae85-4c4c-998c-035cd53b1230" />


**Analysis in progress** — transcript, doctor's guidance, and generated voice response:

![Doctor's guidance and voice response]  <img width="1497" height="716" alt="Screenshot 2026-09-13 005711" src="https://github.com/user-attachments/assets/8175532b-dab0-47a3-afc1-369a9571be93" />

---

## Table of Contents

- [Screenshots](#screenshots)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installing System Dependencies](#installing-system-dependencies)
- [Installing uv](#installing-uv)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Running the App](#running-the-app)
- [Usage](#usage)
- [Useful uv Commands](#useful-uv-commands)
- [Python Dependencies](#python-dependencies)
- [Development Notes](#development-notes)
- [Troubleshooting](#troubleshooting)
- [Security](#security)

---

## How It Works

| Component | Role |
|---|---|
| **Gradio** | Web interface |
| **Groq Whisper** | Transcribes patient voice input |
| **Groq vision model** | Generates skin guidance from image + transcript |
| **Deepgram TTS** | Converts the written response into a spoken doctor-style reply |
| **uv** | Manages the Python version, virtual environment, dependencies, and lockfile |

---

## Project Structure

```
ai-skin-specialist/
├── main.py                     # Gradio application entry point
├── voice_of_the_patient.py     # Microphone recording helper + Groq transcription
├── brain_of_the_doctor_groq.py # Groq vision/text response generation (active in main.py)
├── brain_of_the_doctor.py      # Alternative MiniMax/Anthropic-compatible implementation
├── voice_of_the_doctor.py      # Deepgram text-to-speech generation
├── free_text_to_speech.py      # Additional TTS experiment/helper
├── sample.env                  # Environment variable template
├── pyproject.toml              # Python package metadata and dependencies
├── uv.lock                     # Locked dependency versions
├── .python-version             # Python version pinned for uv/pyenv
└── README.md
```

---

## Requirements

- Python 3.11 or newer
- [uv](https://github.com/astral-sh/uv) package manager
- **FFmpeg** — required by `pydub` and other audio tooling
- **PortAudio** — required by `pyaudio` / `speech_recognition` for microphone support
- API keys for **Groq** and **Deepgram**

---

## Installing System Dependencies

Install FFmpeg and PortAudio *before* running `uv sync` — this avoids most `pyaudio` and microphone-related build errors.

### macOS (Homebrew)

```bash
brew update
brew install ffmpeg portaudio
```

Verify:

```bash
ffmpeg -version
brew list portaudio
```

If `pyaudio` fails to build, confirm Homebrew's PortAudio is discoverable:

```bash
brew --prefix portaudio
```

> Apple Silicon Macs typically use `/opt/homebrew`; Intel Macs typically use `/usr/local`.

### Windows

**Chocolatey** (Administrator PowerShell):

```powershell
choco install ffmpeg portaudio
```

**Scoop** (alternative):

```powershell
scoop install ffmpeg
scoop install portaudio
```

Verify:

```powershell
ffmpeg -version
```

**Notes:**
- Restart your terminal after installing FFmpeg so PATH changes take effect.
- If `pyaudio` fails to install, install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/), then run `uv sync` again.
- Some setups can install `pyaudio` from a prebuilt wheel automatically — if not, missing PortAudio or C++ build tools are the usual cause.

### Linux

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev python3-dev build-essential
```

**Fedora:**

```bash
sudo dnf install ffmpeg portaudio-devel python3-devel gcc gcc-c++ make
```

**Arch Linux:**

```bash
sudo pacman -S ffmpeg portaudio base-devel
```

Verify:

```bash
ffmpeg -version
```

> If microphone access fails on Linux, confirm your audio stack is working and that your user has permission to access the input device.

---

## Installing uv

`uv` handles the virtual environment, dependencies, and lockfile for this project.

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal (or reload your shell config), then verify:

```bash
uv --version
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart PowerShell, then verify:

```powershell
uv --version
```

**Alternative installation methods:**

```bash
pipx install uv
# or
pip install uv
```

---

## Setup

Clone or open the project folder, then run:

```bash
uv sync
```

This reads `pyproject.toml` and `uv.lock`, creates `.venv` if needed, installs Python 3.11 (if your `uv` setup supports managed Python downloads), and installs all locked dependencies.

To force a specific Python version:

```bash
uv python install 3.11
uv sync --python 3.11
```

---

## Environment Variables

Copy the provided template:

```bash
cp sample.env .env
```

Then fill in your values:

```env
GROQ_API_KEY=your_groq_api_key_here
DEEPGRAM_API_KEY=your_deepgram_api_key_here

# Optional model overrides
WHISPER_MODEL=whisper-large-v3
GROQ_MODEL=meta-llama/llama-4-scout-17b-16e-instruct
DEEPGRAM_TTS_MODEL=aura-2-thalia-en

# Optional — only needed if using brain_of_the_doctor.py instead of brain_of_the_doctor_groq.py
MINIMAX_API_KEY=your_minimax_api_key_here
MINIMAX_BASE_URL=https://api.minimax.io/anthropic
MINIMAX_MODEL=MiniMax-M3
```

**Required for the default flow (`main.py`):**
- `GROQ_API_KEY` — audio transcription and image analysis
- `DEEPGRAM_API_KEY` — doctor voice response generation

> Never commit real API keys to version control.

---

## Running the App

```bash
uv run python main.py
```

Gradio will print a local URL, typically:

```
http://127.0.0.1:7860
```

Open it in your browser to use the app.

---

## Usage

1. Record or upload a **patient voice description**.
2. Upload a **skin image** — the current Groq implementation requires one.
3. *(Optional)* Upload a skin video — note that it is **not processed directly**; the app falls back to the uploaded image as the visual reference.
4. Click **Analyze Concern**.
5. Review the transcript, doctor guidance, and generated audio response.

---

## Useful uv Commands

```bash
# Create/update the virtual environment from pyproject.toml and uv.lock
uv sync

# Run the Gradio app
uv run python main.py

# Run an individual module or script
uv run python voice_of_the_patient.py

# Add a dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a dependency
uv remove package-name

# Update the lockfile without installing
uv lock

# Upgrade dependencies within allowed version ranges
uv lock --upgrade

# List installed packages
uv pip list

# Show dependency tree
uv tree
```

You typically don't need to manually activate the virtual environment when using `uv run`. If you want to anyway:

| OS | Command |
|---|---|
| macOS/Linux | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows CMD | `.venv\Scripts\activate.bat` |

Deactivate with:

```bash
deactivate
```

---

## Python Dependencies

Defined in `pyproject.toml`:

- **gradio** — web app interface
- **groq** — Whisper transcription and vision/chat model
- **deepgram-sdk** — text-to-speech
- **anthropic** — alternate MiniMax-compatible implementation
- **python-dotenv** — loads `.env` values
- **pydub**, **pyaudio**, **sounddevice**, **speechrecognition** — audio recording/conversion
- **pillow** — image resizing and encoding before sending to Groq
- **numpy**, **path** — supporting utilities

Since this project ships a `uv.lock`, prefer `uv sync` over `pip install -r requirements.txt` — there is no `requirements.txt` in this project.

---

## Development Notes

- `main.py` imports `brain_of_the_doctor` from **`brain_of_the_doctor_groq.py`**.
- `brain_of_the_doctor_groq.py` **requires an image**. If only a video is uploaded, form validation passes, but Groq vision will raise an error since no image was provided.
- `brain_of_the_doctor.py` is an alternate MiniMax/Anthropic-compatible implementation that can encode either image *or* video — but it is **not** the active import in `main.py`.
- Generated audio is written to `doctor_response.mp3` by default.
- Gradio launches with `debug=True` in `main.py`.

---

## Troubleshooting

<details>
<summary><strong>FFmpeg not found</strong></summary>

Install FFmpeg for your OS (see [above](#installing-system-dependencies)), restart your terminal, and verify:

```bash
ffmpeg -version
```
</details>

<details>
<summary><strong>pyaudio fails to install</strong></summary>

Usually caused by missing PortAudio headers or build tools:

- **macOS:** `brew install portaudio`
- **Windows:** Install PortAudio + Microsoft C++ Build Tools, then re-run `uv sync`
- **Ubuntu/Debian:** `sudo apt install portaudio19-dev python3-dev build-essential`
- **Fedora:** `sudo dnf install portaudio-devel python3-devel gcc gcc-c++ make`
- **Arch:** `sudo pacman -S portaudio base-devel`
</details>

<details>
<summary><strong>Microphone not detected</strong></summary>

- Check OS-level microphone permissions.
- Close other apps that may be using the microphone.
- Confirm your browser has mic permission for the local Gradio URL.
- Confirm PortAudio is installed.
</details>

<details>
<summary><strong>Missing API key errors</strong></summary>

Make sure `.env` exists in the project root and contains at least:

```env
GROQ_API_KEY=your_groq_api_key_here
DEEPGRAM_API_KEY=your_deepgram_api_key_here
```

Then run the app from the project root:

```bash
uv run python main.py
```
</details>

<details>
<summary><strong>Deepgram audio generation fails</strong></summary>

Check that `DEEPGRAM_API_KEY` is valid and that the selected `DEEPGRAM_TTS_MODEL` is available for your account.
</details>

<details>
<summary><strong>Groq image analysis fails</strong></summary>

Check that `GROQ_API_KEY` is valid and that `GROQ_MODEL` supports image input. By default, uploaded images are converted to JPEG, resized to fit within 1024×1024, and sent as a base64 data URL.
</details>

---

## Security

- Keep `.env` private and out of version control.
- Never commit real API keys.
- Treat patient images, videos, and audio as sensitive data.
- Sample media is included for local testing only — production use should define a clear data retention and privacy policy.

---

## Medical Disclaimer

This app is an AI assistant for **general skin care information**. It cannot diagnose disease, prescribe medication, or replace a medical professional. For severe symptoms, rapid spreading, fever, pain, bleeding, signs of infection, or any urgent concern, contact a licensed clinician immediately.
