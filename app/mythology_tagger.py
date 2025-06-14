# MythologyTagger – Label Sentences Involving Supernatural or Mythic Events

import re

keywords = [
    "transformed", "spirit", "appeared", "vanished", "sky",
    "underworld", "dream", "cursed", "sacred", "eternal"
]

def tag_myth_sentences(text):
    sentences = re.split(r'[.!?]', text)
    tagged = []
    for s in sentences:
        if any(k in s.lower() for k in keywords):
            tagged.append((s.strip(), "MYTHIC"))
        else:
            tagged.append((s.strip(), "NORMAL"))
    return [t for t in tagged if t[0]]

# Example
if __name__ == '__main__':
    sample = "Túpanax vanished into the sky. The people gathered firewood. Dreams warned them of the underworld."
    for sent, tag in tag_myth_sentences(sample):
        print(f"[{tag}] {sent}")
