# GeoHymnSynth - Turn Place Names into Chant Structures

import random
import re

# Phonetic transformation map for chant syllables
chant_map = {
    'a': 'ah', 'e': 'eh', 'i': 'ee', 'o': 'oh', 'u': 'oo',
    'j': 'y', 'll': 'ly', 'v': 'b', 'z': 's', 'x': 'ks',
    'c': 'k', 'qu': 'kw', 'ñ': 'ny'
}

def syllabify(name):
    name = name.lower()
    name = re.sub(r'[^a-zñ ]', '', name)
    for k, v in chant_map.items():
        name = name.replace(k, v)
    syllables = re.findall(r'[aeiou]{1,2}|[^aeiou ]+', name)
    return [s for s in syllables if s.strip()]

def chant_lines(name, reps=3):
    syllables = syllabify(name)
    line = "-".join(syllables).capitalize()
    return [line for _ in range(reps)]

# Example use
if __name__ == '__main__':
    places = ["Temecula", "La Jolla", "Tamalpais", "Yerba Buena"]
    for place in places:
        print(f"\nChant for {place}:")
        for line in chant_lines(place):
            print(line)
