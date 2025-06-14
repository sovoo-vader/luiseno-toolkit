# TTSSynthesizer – Generate Luiseño Speech from Phoneme Sequences

from gtts import gTTS
import os

# Simulated IPA-to-speakable phoneme conversion (would be language-specific)
phoneme_map = {
    "m": "m",
    "i": "ee",
    "y": "y",
    "a": "ah",
    "x": "sh",
    "t": "t",
    "u": "oo",
    "p": "p",
    "n": "n"
}

def convert_to_pronounceable(phoneme_seq):
    return ' '.join(phoneme_map.get(p, p) for p in phoneme_seq)

def synthesize_luiseno(phoneme_seq, filename="output.mp3"):
    text = convert_to_pronounceable(phoneme_seq)
    print(f"🗣️ Synthesizing: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"start {filename}" if os.name == 'nt' else f"afplay {filename}")

# Example use
if __name__ == '__main__':
    synthesize_luiseno(["m", "i", "y", "a", "x"])
