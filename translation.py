from googletrans import Translator, LANGUAGES

translator = Translator()

def detect_language(text):
    """Detects the language of the given text."""
    try:
        detected = translator.detect(text)
        return detected.lang if detected and detected.lang else "en"
    except Exception as e:
        print("Language detection error:", e)
        return "en"

def translate_text(text, target_language):
    """Translates text to the target language."""
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text if translated and translated.text else text
    except Exception as e:
        print("Translation error:", e)
        return text

def get_language_name(lang_code):
    """Gets the language name from the language code."""
    try:
        return LANGUAGES.get(lang_code, "Unknown")
    except Exception as e:
        print("Language name retrieval error:", e)
        return "Unknown"
