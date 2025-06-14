# BasketLang – DSL for Designing Intent-Encoded Basket Sequences

syntax_guide = {
    "MOTIF": "Named motif keyword (e.g. 'waxpoo')",
    "REPEAT N": "Repeat the last motif N times",
    "COLOR name": "Set symbolic color for next motif (e.g. red, black, ochre)",
    "PAUSE": "Hold stitch – symbolic silence",
    "END": "Terminate pattern"
}

motif_meanings = {
    "waxpoo": "centeredness",
    "vutsierau": "sacred boundary",
    "qaxkwilee": "searching or flow",
    "venii-gemaa": "strike, flint, spark",
    "tcwal mila": "grounding or stability"
}

color_symbols = {
    "red": "life force",
    "black": "mourning",
    "ochre": "earth and ancestors"
}


def interpret_script(script):
    lines = script.strip().splitlines()
    stack = []
    current_color = None

    for line in lines:
        tokens = line.strip().split()
        if not tokens:
            continue
        cmd = tokens[0].upper()

        if cmd == "MOTIF":
            motif = tokens[1]
            meaning = motif_meanings.get(motif, "unknown")
            stack.append(f"🧶 {motif} ({meaning}) {'in ' + current_color if current_color else ''}")
        elif cmd == "REPEAT":
            count = int(tokens[1])
            stack.extend([stack[-1]] * (count - 1))
        elif cmd == "COLOR":
            current_color = tokens[1]
        elif cmd == "PAUSE":
            stack.append("🔕 [pause]")
        elif cmd == "END":
            break

    return stack

# Example use
if __name__ == '__main__':
    code = """
    COLOR red
    MOTIF waxpoo
    REPEAT 2
    COLOR black
    MOTIF vutsierau
    PAUSE
    MOTIF qaxkwilee
    END
    """
    output = interpret_script(code)
    for line in output:
        print(line)
