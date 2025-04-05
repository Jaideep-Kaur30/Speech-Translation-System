# Speech Translation System

## Overview
**A real-time speech translation system that converts spoken words to text, translates to a target language, and speaks the translation.**

### Purpose
- Bridge language barriers through voice-based communication
- Demonstrate integration of speech recognition, translation, and text-to-speech technologies
- Provide instant multilingual audio translation capabilities

### Scope
- Real-time speech-to-text conversion
- Support for 100+ languages via Google Translate
- Audio output of translated text
- Cross-platform compatibility (with OS-specific audio handling)

## ✨ Key Features
- 🎤 Voice input recognition
- 🌐 Multi-language translation
- 🔊 Audio output generation
- 🛠 Error handling for speech recognition failures
- 📦 Modular architecture for easy maintenance

## 🛠 Installation
```bash
pip install SpeechRecognition googletrans==4.0.0-rc1 gtts pyaudio

🚀 Usage
  -Run the script: python3 speech_rec.py

  -Speak when you see "Listening..."

  -Enter target language code (e.g., 'es' for Spanish, 'fr' for French)

  -Hear the translated audio output

Example language codes:

  -Hindi: 'hi' | Punjabi: 'pa'
  
  -Spanish: 'es' | French: 'fr'

  -German: 'de' | Japanese: 'ja'

##📁 Code Structure
Core Components
def recognize_speech():
  -Captures audio input and converts to text using Google Speech Recognition
    # Uses PyAudio for microphone access
    # Implements error handling for unclear audio

def translate_text(text, target_lang):
  -Translates text using Googletrans with language validation
    # Supports all Google Translate languages
    # Returns both translated text and pronunciation

def text_to_speech(text, lang):
  -Converts translated text to speech using gTTS
    # Generates MP3 output file
    # Implements OS-specific audio playback

Main Workflow
def main():
    # Speech-to-Text
    original_text = recognize_speech()
    
    # Language Selection
    target_lang = input("Enter target language code: ")
    
    # Text Translation
    translated_text = translate_text(original_text, target_lang)
    
    # Audio Output
    text_to_speech(translated_text, target_lang)

⚙️ Technical Highlights
  -Audio Handling:
    os.system("afplay translated_output.mp3")  # macOS
    # Replace with 'start' for Windows or 'mpg123' for Linux

  -Translation Validation:
    translator.translate(text, dest=target_lang)

  -Real-time Processing:
    with sr.Microphone() as source:
    audio = r.listen(source)  # Continuous audio stream capture




