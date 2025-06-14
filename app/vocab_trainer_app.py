# VocabTrainerApp – Flashcard Quiz for Luiseño Morphemes

import random

morpheme_flashcards = [
    ("míyax", "go"),
    ("túpanax", "coyote"),
    ("yawúsh", "howl"),
    ("teméq", "tomorrow"),
    ("noona", "I")
]

def run_quiz(cards):
    random.shuffle(cards)
    score = 0
    for luiseño, gloss in cards:
        ans = input(f"What is the meaning of '{luiseño}'? ").strip().lower()
        if ans == gloss:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. Correct answer: {gloss}")
    print(f"\nFinal Score: {score}/{len(cards)}")

if __name__ == '__main__':
    run_quiz(morpheme_flashcards)