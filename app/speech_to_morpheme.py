# SpeechToMorpheme – Real-Time Recognition of Luiseño Morphemes from Spoken Input

import speech_recognition as sr

known_morphemes = ["míyax", "túpanax", "yawúsh", "noona", "teméq"]

def recognize_morpheme():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak a Luiseño morpheme:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"🔊 You said: {text}")
        match = [m for m in known_morphemes if m in text]
        if match:
            print(f"✅ Recognized morpheme(s): {', '.join(match)}")
        else:
            print("❌ No known morphemes detected.")
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError as e:
        print(f"🔌 Speech recognition error: {e}")

# Example use
if __name__ == '__main__':
    recognize_morpheme()