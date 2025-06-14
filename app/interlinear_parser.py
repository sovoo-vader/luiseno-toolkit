# Interlinear Parser – Extract Morphemes and Glosses from Structured Interlinear Text

import re

def parse_interlinear(text):
    """
    Example format:
    line1: Luiseño morphemes
    line2: gloss (English)
    line3: free English translation
    """
    lines = text.strip().split("\n")
    triples = []
    for i in range(0, len(lines), 3):
        if i+2 < len(lines):
            l1, l2, l3 = lines[i], lines[i+1], lines[i+2]
            morphemes = l1.split()
            glosses = l2.split()
            if len(morphemes) != len(glosses):
                glosses += ["-"] * (len(morphemes) - len(glosses))
            triples.append(list(zip(morphemes, glosses, [l3]*len(morphemes))))
    return triples

# Example
if __name__ == '__main__':
    sample = """
    noona míyax teméq
    I.SUB go.PRES tomorrow
    I will go tomorrow

    túpanax kú’xal yawúsh
    Coyote PST howl.PRES
    The coyote howled
    """
    parsed = parse_interlinear(sample)
    for line in parsed:
        for m, g, e in line:
            print(f"{m:10s} | {g:10s} | {e}")
        print("-")
