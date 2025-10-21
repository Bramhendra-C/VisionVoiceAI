import speech_recognition as sr
import pygame
import datetime
import webbrowser
import pywhatkit as kit
import random
import pyttsx3
import wikipedia
import pyjokes
import requests
import os
# import FaceMode  # Make sure you have a FaceMode.py file with a face() function

# --- CONFIGURATION ---
# It's better to load sensitive data like API keys from environment variables or a config file
# For now, we'll keep it here but remind the user to replace it.
OPENWEATHERMAP_API_KEY = "80590db90b5686dc7b68057edb05d6ec"
MUSIC_DIR = "path/to/your/music_folder" # Specify a directory to save downloaded music

# --- DATA ---
FUN_FACTS = [
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils. Archaeologists have found edible honey in ancient tombs.",
    "Octopuses have three hearts.",
    "Sharks existed before trees.",
    "A day on Venus is longer than a year on Venus."
]

QUOTES = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don't let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Do something today that your future self will thank you for."
]

# --- INITIALIZATION ---
try:
    engine = pyttsx3.init()
    wikipedia.set_lang("en")
    pygame.mixer.init()
except Exception as e:
    print(f"Error during initialization: {e}")
    exit()

# --- CORE FUNCTIONS ---
def speak(text):
    """Converts text to speech."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listens for a command and returns it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return "none"
    except sr.RequestError as e:
        speak("Could not request results from the speech recognition service.")
        print(f"Speech Recognition Error: {e}")
        return "none"
    except Exception as e:
        speak("An unexpected error occurred while capturing your command.")
        print(f"Error: {e}")
        return "none"

# --- HELPER FUNCTIONS FOR COMMANDS ---
def get_weather(city):
    """Fetches and speaks the weather for a given city."""
    if not OPENWEATHERMAP_API_KEY or OPENWEATHERMAP_API_KEY == "Paste-Your-OpenWeatherMap-API-Key-Here":
        speak("Weather check failed. Please set your OpenWeatherMap API key in the script.")
        return

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            speak(f"The current temperature in {city} is {temp} degrees Celsius with {desc}.")
        else:
            speak(f"I couldn't find weather information for {city}. The server said: {data.get('message', 'Unknown error')}")

    except requests.exceptions.HTTPError as http_err:
        speak(f"An HTTP error occurred while fetching weather")
    except Exception as e:
        speak(f"Sorry, an error occurred while retrieving weather information.")

def download_and_play_youtube_audio(song_name, download_path):
    """
    Placeholder function: Downloads audio from a YouTube video and returns the file path.
    You need to implement this using a library like `yt_dlp` or `pytube`.
    """
    speak(f"Searching for {song_name} to download.")
    # ---- EXAMPLE IMPLEMENTATION (requires `yt_dlp` and `ffmpeg`) ----
    # try:
    #     from yt_dlp import YoutubeDL
    #     if not os.path.exists(download_path):
    #         os.makedirs(download_path)
    #
    #     ydl_opts = {
    #         'format': 'bestaudio/best',
    #         'postprocessors': [{
    #             'key': 'FFmpegExtractAudio',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '192',
    #         }],
    #         'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
    #         'default_search': 'auto',
    #     }
    #     with YoutubeDL(ydl_opts) as ydl:
    #         info = ydl.extract_info(song_name, download=True)['entries'][0]
    #         filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
    #         speak(f"Downloaded {info['title']}. Now playing.")
    #         return filename
    # except Exception as e:
    #     speak(f"Sorry, I couldn't download the song. Error: {e}")
    #     return None
    # -----------------------------------------------------------------
    speak("Download functionality is not yet implemented.")
    return None

def wish_user():
    """Greets the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    speak(f"{greeting} I am your assistant. How can I help you today?")

# --- MAIN ASSISTANT LOGIC ---
def run_assistant():
    """Main function to run the voice assistant."""
    wish_user()
    is_music_playing = False
    volume = 0.5
    pygame.mixer.music.set_volume(volume)

    while True:
        #query = take_command()
        query = input("You : ").lower()  # For testing without voice input
        if query == "none":
            continue
        if 'time' in query:
            speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'fun fact' in query:
            speak(random.choice(FUN_FACTS))
        
        elif 'quote' in query:
            speak(random.choice(QUOTES))

        # --- Web Search and Actions ---
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            search_term = query.replace("wikipedia", "").strip()
            try:
                summary = wikipedia.summary(search_term, sentences=random.randint(2, 4))
                speak("According to Wikipedia")
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"The topic '{search_term}' is ambiguous. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I could not find a Wikipedia page for '{search_term}'.")
            except Exception as e:
                speak(f"An error occurred while searching Wikipedia: {e}")

        elif 'youtube' in query:
            search_term = query.replace('open', "").replace('search', "").replace('youtube', "").replace('play', "").strip()
            if not search_term:
                speak("What should I play on YouTube?")
                search_term = take_command()
                #search_term = input("You : ").lower()  # For testing without voice input
            if search_term and search_term != "none":
                speak(f"Playing {search_term} on YouTube")
                kit.playonyt(search_term)
        
        elif 'search' in query or 'google' in query:
            search_term = query.replace("search", "").replace("google", "").strip()
            speak(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")

        elif 'weather' in query:
            city = query.replace("weather in", "").replace("what's the weather in", "").strip()
            if city:
                get_weather(city)
            else:
                speak("Please tell me the city name for the weather forecast.")

        # --- Music Controls ---
        elif 'play online' in query or 'online song' in query:
            song_name = query.replace("play online", "").replace("online song", "").strip()
            file_path = download_and_play_youtube_audio(song_name, MUSIC_DIR)
            if file_path:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                is_music_playing = True

        elif 'pause' in query and is_music_playing:
            pygame.mixer.music.pause()
            speak("Music paused.")
        
        elif 'resume' in query and is_music_playing:
            pygame.mixer.music.unpause()
            speak("Resuming music.")

        elif 'volume up' in query:
            volume = min(1.0, volume + 0.1)
            pygame.mixer.music.set_volume(volume)
            speak(f"Volume set to {int(volume * 100)} percent.")

        elif 'volume down' in query:
            volume = max(0.0, volume - 0.1)
            pygame.mixer.music.set_volume(volume)
            speak(f"Volume set to {int(volume * 100)} percent.")

        # --- Exit Command ---
        elif 'exit' in query or 'stop' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break


