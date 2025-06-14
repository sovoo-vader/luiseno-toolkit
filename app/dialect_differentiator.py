# DialectDifferentiator – Compare Dialects for Phonological and Lexical Differences

from difflib import ndiff

# Simulated dialect entries
rincon = {
    "coyote": "túpanax",
    "moon": "meeláx",
    "sun": "néeyu"
}
other_dialect = {
    "coyote": "túpanash",
    "moon": "meláx",
    "sun": "néyo"
}

def compare_dialects(word):
    rin = rincon.get(word)
    oth = other_dialect.get(word)
    if not rin or not oth:
        return f"❌ Word '{word}' not found in one or both dialects."
    diff = list(ndiff([rin], [oth]))
    return f"Rincón: {rin}\nOther:  {oth}\nDiff:   {''.join(diff)}"

# Example use
if __name__ == '__main__':
    print(compare_dialects("moon"))
