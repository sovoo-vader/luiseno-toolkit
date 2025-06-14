# PhonemeAnalyzer – Count and Categorize Phoneme Frequencies in Luiseño Text

from collections import Counter
import re

# Luiseño phoneme set (simplified)
phonemes = ["a", "e", "i", "o", "u", "p", "t", "k", "q", "m", "n", "l", "r", "s", "sh", "x", "ch", "w", "y", "h"]

def tokenize_phonemes(text):
    # Very simplified, real parsing would use IPA or phonemic transcription
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    found = []
    for word in tokens:
        i = 0
        while i < len(word):
            if word[i:i+2] in phonemes:
                found.append(word[i:i+2])
                i += 2
            elif word[i] in phonemes:
                found.append(word[i])
                i += 1
            else:
                i += 1
    return Counter(found)

# Example use
if __name__ == '__main__':
    corpus = "Noona míyax túpanax yawúsh míyax túpanax"
    result = tokenize_phonemes(corpus)
    for ph, count in result.most_common():
        print(f"{ph:4s} : {count}")
