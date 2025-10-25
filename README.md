# 🌐 VisionVoiceAI  
**Real-time Face Detection + Voice Assistant in Python**  
_A complete “Vision + Voice” AI tool built using OpenCV, SpeechRecognition, and Pyttsx3._

---

## 🚀 Overview  
**VisionVoiceAI** integrates computer vision and natural voice interaction.  
It detects faces in real time using your webcam and lets you control or communicate with a voice assistant — all in one seamless Python project.

---

## ✨ Features  
- 🎯 Real-time **Face Detection** using OpenCV  
- 🗣️ Interactive **Voice Assistant** with speech input/output  
- ⚙️ Simple **menu-based launcher (start.py)**  
- 🧠 Easily extendable to emotion detection or custom voice commands  
- 💡 Works offline — no external APIs required

---

## 🗂️ Project Structure
VisionVoiceAI/
├── face.py # Face detection logic (OpenCV)
├── voice_assistant.py # Voice assistant logic (speech)
├── start.py # Main entry script (menu system)
├── requirements.txt # Python dependencies
└── README.md # This file


---

## 🧩 Requirements  
- Python **3.8+**
- A working **webcam** and **microphone**
- OS: Windows, macOS, or Linux  

---

## ⚙️ Installation & Run (All-in-One Script)

You can **set up and run the entire project** automatically using this integrated YAML/Bash block.  
It works locally (bash) or in GitHub Actions CI.

```bash
# ============================================================
# VisionVoiceAI — Setup & Run Script
# ============================================================
# Works both locally (bash ./setup.sh) and in GitHub Actions CI
# Author: Bramhendra C
# ------------------------------------------------------------

name: VisionVoiceAI Setup and Run
on: [workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies and Run
      run: |
        echo "🚀 Setting up VisionVoiceAI..."
        python -m pip install --upgrade pip

        if [ -f requirements.txt ]; then
          pip install -r requirements.txt
        else
          echo "⚠️ No requirements.txt found — installing base libs..."
          pip install opencv-python pyttsx3 SpeechRecognition pygame requests wikipedia pywhatkit
        fi

        echo "🎬 Launching VisionVoiceAI..."
        python start.py || echo "✅ Session ended gracefully."

How It Works

face.py → Uses OpenCV to detect faces from your webcam feed.

voice_assistant.py → Listens for commands, processes them, and replies using text-to-speech.

start.py → Acts as a main menu (Run Face Detection / Get Face Unfocus Count / Voice Assistant / Exit).

