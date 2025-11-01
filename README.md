# Kokoro TTS Web App (English Only)

A Flask web app that converts text to speech using Kokoro TTS.  
Currently supports English voices only.

---

## Project Structure

kokoro_tts_webapp/
├─ app.py
├─ templates/index.html
├─ static/
│ └─ output_*.wav # auto-generated, ignored by git
├─ .gitignore
├─ requirements.txt
└─ README.md


---

## Setup

1. Create a virtual environment:

```bash
python -m venv venv

Activate the environment:

Windows: venv\Scripts\activate

Linux/macOS: source venv/bin/activate

Install packages:

pip install -r requirements.txt


Download Kokoro TTS English model and voices:

kokoro-v1.0.onnx

voices-v1.0.bin

Place them in:

C:\Users\<username>\.cache\kokoro\   (Windows)

Running
python app.py


Open http://127.0.0.1:5000
 in your browser.

Usage

Enter text

Select a voice

Click "Play" to generate speech

Download the output .wav if needed

Notes

Japanese text may not be pronounced correctly with English voices

Japanese TTS support will be added once Kokoro provides Japanese model & voices
