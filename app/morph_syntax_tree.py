# MorphSyntaxTreeBuilder – Generate Syntax Trees from Morpheme-Gloss Sequences

import nltk
from nltk import CFG

# Define a basic CFG for demo purposes (non-linguistically accurate)
# In practice, rules would need to match Luiseño morphology exactly

grammar = CFG.fromstring("""
S -> NP VP
NP -> PRON | DET N
VP -> V NP | V ADV
PRON -> 'I'
DET -> 'the'
N -> 'coyote'
V -> 'howled' | 'goes'
ADV -> 'quickly'
""")

parser = nltk.ChartParser(grammar)

def parse_example(tokens):
    print(f"Input: {' '.join(tokens)}")
    for tree in parser.parse(tokens):
        tree.pretty_print()
        tree.draw()

# Example (English gloss-based demo)
if __name__ == '__main__':
    tokens = ['I', 'goes']
    parse_example(tokens)

def main():
    import streamlit as st
    st.subheader("Morph Syntax Tree Demo")
    st.markdown("Try running this on a simple English gloss.")
    tokens = st.text_input("Enter tokens (e.g. `I goes`):").split()
    if tokens:
        from nltk import CFG, ChartParser

        grammar = CFG.fromstring(\"\"\"
        S -> NP VP
        NP -> PRON | DET N
        VP -> V NP | V ADV
        PRON -> 'I'
        DET -> 'the'
        N -> 'coyote'
        V -> 'howled' | 'goes'
        ADV -> 'quickly'
        \"\"\")
        parser = ChartParser(grammar)
        for tree in parser.parse(tokens):
            st.text(tree)
