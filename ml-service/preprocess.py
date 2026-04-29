from langdetect import detect
from deep_translator import GoogleTranslator

def preprocess_text(text):
    try:
        if detect(text) != 'en':
            text = GoogleTranslator(source='auto', target='en').translate(text)
    except:
        pass
    return text.lower()