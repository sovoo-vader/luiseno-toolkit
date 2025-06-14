# AlignmentTool – Align Parallel Luiseño and English Sentences for Study or Translation

from difflib import SequenceMatcher

luiseno_lines = [
    "noona míyax teméq",
    "túpanax yawúsh",
    "míyax túpanax"
]

english_lines = [
    "I will go tomorrow",
    "The coyote howled",
    "Coyote goes"
]

def align_parallel_text(luiseno, english):
    alignment = list(zip(luiseno, english))
    for i, (lu, en) in enumerate(alignment):
        score = SequenceMatcher(None, lu, en).ratio()
        print(f"[{i+1}] 🗣️ {lu} ↔️ {en}\n   🔍 Similarity Score: {score:.2f}\n")

# Example use
if __name__ == '__main__':
    align_parallel_text(luiseno_lines, english_lines)
