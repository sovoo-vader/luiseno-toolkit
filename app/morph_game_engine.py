# MorphGameEngine – Gamify Morpheme Recognition and Matching

import random

morpheme_bank = [
    {"form": "míyax", "gloss": "go"},
    {"form": "noona", "gloss": "I"},
    {"form": "túpanax", "gloss": "coyote"},
    {"form": "teméq", "gloss": "tomorrow"},
    {"form": "yawúsh", "gloss": "howl"}
]

def play_match_game():
    score = 0
    pairs = random.sample(morpheme_bank, len(morpheme_bank))
    for morph in pairs:
        choice = input(f"Match the gloss: '{morph['gloss']}' → ").strip().lower()
        if choice == morph['form']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. It was '{morph['form']}'")
    print(f"\nScore: {score}/{len(morpheme_bank)}")

# Example use
if __name__ == '__main__':
    play_match_game()
