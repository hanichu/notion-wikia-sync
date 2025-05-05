# Handles DeepL and Google Translate fallback

import os
import deepl
from googletrans import Translator as GoogleTranslator
from dotenv import load_dotenv

load_dotenv()

deepl_api_key = os.getenv("DEEPL_API_KEY")
deepl_translator = deepl.Translator(deepl_api_key)
google_translator = GoogleTranslator()

def translate_text(text, source_lang, target_lang):
    try:
        result = deepl_translator.translate_text(
            text, source_lang=source_lang, target_lang=target_lang
        )
        return result.text
    except Exception as deepl_error:
        print("DeepL failed, falling back to Google:", deepl_error)
        try:
            result = google_translator.translate(text, src=source_lang.lower(), dest=target_lang.lower())
            return result.text
        except Exception as google_error:
            print("Google Translate failed:", google_error)
            return None
# Handles DeepL and Google Translate fallback

import os
import deepl
from googletrans import Translator as GoogleTranslator
from dotenv import load_dotenv

load_dotenv()

deepl_api_key = os.getenv("DEEPL_API_KEY")
deepl_translator = deepl.Translator(deepl_api_key)
google_translator = GoogleTranslator()

def translate_text(text, source_lang, target_lang):
    try:
        result = deepl_translator.translate_text(
            text, source_lang=source_lang, target_lang=target_lang
        )
        return result.text
    except Exception as deepl_error:
        print("DeepL failed, falling back to Google:", deepl_error)
        try:
            result = google_translator.translate(text, src=source_lang.lower(), dest=target_lang.lower())
            return result.text
        except Exception as google_error:
            print("Google Translate faile:", google_error)
            return None
