import speech_recognition as sr
from langdetect import detect
import pyttsx3
import sys

# Ensure terminal uses UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

def record_audio():
    """Records audio from the microphone and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Error: Check your internet connection."

def generate_response(text):
    """Detect the language and return the text and language code."""
    lang = detect(text)
    return text, lang

def speak_text(text, lang='en'):
    """Speaks the given text using pyttsx3 (offline TTS)."""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        
        # Optional: Set language-specific voice if available
        voices = engine.getProperty('voices')
        if lang.startswith('hi'):  # Example: Hindi
            for voice in voices:
                if 'hindi' in voice.name.lower() or 'hi' in voice.languages:
                    engine.setProperty('voice', voice.id)
                    break
        elif lang.startswith('en'):
            for voice in voices:
                if 'english' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("🔊 Speech synthesis error:", e)

# Example for testing
if __name__ == "__main__":
    user_input = record_audio()
    if user_input not in ["Sorry, I couldn't understand that.", "Error: Check your internet connection."]:
        response, lang = generate_response(user_input)
        print(f"Detected language: {lang}")
        print("Bot:", response)
        speak_text(response, lang)
