# MemoryBasketCompiler – Digitally Encode Personal or Ancestral Memories into Motif Sequences

memory_tags = {
    "birth": "waxpoo – centerline marker",
    "first hunt": "venii-gemaa – spark, activation",
    "grief": "tcwal mila – frog hand, anchor",
    "dream": "apxanko'ikoi – ascension steps",
    "ancestor": "vutsierau – continuity ring",
    "journey": "qaxkwilee – sturgeon-back path"
}

def compile_memory_basket(events):
    compiled = []
    for e in events:
        motif = memory_tags.get(e.lower(), "unknown segment")
        compiled.append(f"[{e} → {motif}]")
    return compiled

# Example use
if __name__ == '__main__':
    sequence = ["birth", "dream", "grief", "journey"]
    result = compile_memory_basket(sequence)
    print("🧺 Memory Basket Sequence:")
    for r in result:
        print(f" - {r}")
