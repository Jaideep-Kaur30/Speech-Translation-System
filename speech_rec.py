import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        print("\nYou said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError:
        print("Speech service unavailable")
        return None

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    print(f"\nTranslated to {target_lang}: {translation.text}")
    return translation.text

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("translated_output.mp3")
    os.system("afplay translated_output.mp3")  # For macOS

def main():
    # Step 1: Capture speech input
    original_text = recognize_speech()
    
    if not original_text:
        return
    
    # Step 2: Get target language from user
    target_lang = input("\nWhich language would you like to translate to? (e.g., 'hi' for Hindi, 'pa' for Punjabi, 'es' for Spanish): ").strip().lower()
    
    # Step 3: Translate the text
    translated_text = translate_text(original_text, target_lang)
    
    # Step 4: Convert translated text to speech
    text_to_speech(translated_text, target_lang)

if __name__ == "__main__":
    main()