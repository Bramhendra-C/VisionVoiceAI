# VisionVoice AI Assistant

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)

A multi-functional assistant built in Python that combines a voice-controlled command center with real-time computer vision capabilities. This project provides a simple command-line menu to access different AI modules, including a versatile voice assistant and a face detection/focus tracker.

## Features

### 🎤 Voice Assistant (`voice_assistant.py`)

A smart assistant that can understand voice commands to perform various tasks:

* **Conversational:** Greets you based on the time of day, tells jokes (`pyjokes`), inspiring quotes, and fun facts.
* **Information Retrieval:**
    * Fetches summaries from **Wikipedia**.
    * Searches **Google** and opens the results in your browser.
    * Checks the current **time**.
* **Actions:**
    * Plays any video/song on **YouTube** (`pywhatkit`).
    * Fetches real-time **weather** for any city (using OpenWeatherMap API).
* **Music Control:**
    * Controls local music playback using `pygame` (pause, resume, volume up/down).
    * Includes a *placeholder* function to download audio from YouTube. (See configuration to enable this).

**Note:** The assistant is currently set to use text input for easy testing. To enable real voice commands, open `voice_assistant.py` and swap these two lines:
```python
#query = take_command()
query = input("You : ").lower()  # For testing without voice input
...to this:

Python

query = take_command()
#query = input("You : ").lower()  # For testing without voice input
📸 Computer Vision (face.py)
Uses your webcam for real-time video processing with OpenCV:

Face Detection: A simple mode that detects faces in real-time and draws a green bounding box around them.

Face Unfocus Counter: A "focus mode" tool.

When a face is detected, it shows a "FOCUSED" status with a green border.

When a face is not detected (i.e., you look away), it shows an "UNFOCUSED" status with a red border and increments a counter.

Setup and Installation
Follow these steps to get the project running on your local machine.

1. Prerequisites
Python 3.7 or newer

A microphone (for the voice assistant)

A webcam (for the face detection)

2. Clone the Repository

# Replace with your actual repository URL
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name
3. Create a Virtual Environment (Recommended)
Bash

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
You will need to create a requirements.txt file for these packages.

requirements.txt

opencv-python
speechrecognition
pyaudio
pygame
pywhatkit
pyttsx3
wikipedia
pyjokes
requests
Install them all with one command:

pip install -r requirements.txt
Note: pyaudio can sometimes be difficult to install. If you have trouble, try installing it manually via pipwin (pip install pipwin && pipwin install pyaudio) or by downloading the wheel file for your system.

⚠️ Important Configuration
Before you can use all features, you must configure the voice_assistant.py file.

1. Get an OpenWeatherMap API Key
The weather feature will not work without a valid API key.

Go to OpenWeatherMap.org and create a free account.

Navigate to the "API keys" tab and copy your default key.

Open voice_assistant.py and paste your key into the OPENWEATHERMAP_API_KEY variable (line 20):

Python

# BEFORE
OPENWEATHERMAP_API_KEY = "80590db90b5686dc7b68057edb05d6ec"

# AFTER (example)
OPENWEATHERMAP_API_KEY = "your_actual_api_key_paste_it_here"
2. Set Your Music Directory
The play online command is designed to download and save music. You must specify a folder where these files should be saved.

Open voice_assistant.py and find the MUSIC_DIR variable (line 21):

Change the placeholder path to a real folder on your computer.

Python

# BEFORE
MUSIC_DIR = "path/to/your/music_folder"

# AFTER (Windows example)
MUSIC_DIR = "C:/Users/YourName/Music/AssistantDownloads"

# AFTER (macOS/Linux example)
MUSIC_DIR = "/home/YourName/Music/AssistantDownloads"
3. (Optional) Enable YouTube Downloads
The function download_and_play_youtube_audio is currently a placeholder. To make it work, you need:

Install yt_dlp: pip install yt_dlp

Install ffmpeg: This is a system-level tool, not a Python package. You must download and install it and add it to your system's PATH.

Uncomment the code: In voice_assistant.py, uncomment lines 106-126 (the example implementation).

How to Run
Once you have installed the dependencies and configured the API key, you can run the main application from your terminal:

python start.py
This will launch the main menu. Simply type the number of the feature you want to use and press Enter.

1. Run Face Detection
2. Get Face Unfocus Count
3. Voice assistant
4. Exit
Select an option: 
To exit the Face Detection or Unfocus Counter, press the 1 key.
To exit the Voice Assistant, say "exit", "stop", or "bye" (or type it if you are in text mode).