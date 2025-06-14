# CustomTokenizer – Luiseño-Compatible Tokenizer for HuggingFace or NLP Pipelines

import re
from typing import List

class LuisenoTokenizer:
    def __init__(self, vocab=None):
        self.vocab = vocab if vocab else {}

    def tokenize(self, text: str) -> List[str]:
        # Normalize input
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = text.split()
        return tokens

    def build_vocab(self, corpus: List[str]):
        token_freq = {}
        for line in corpus:
            for token in self.tokenize(line):
                token_freq[token] = token_freq.get(token, 0) + 1
        self.vocab = {t: i for i, (t, _) in enumerate(sorted(token_freq.items(), key=lambda x: -x[1]))}
        return self.vocab

    def encode(self, text: str) -> List[int]:
        return [self.vocab.get(t, self.vocab.get("<unk>", 0)) for t in self.tokenize(text)]

    def decode(self, tokens: List[int]) -> str:
        rev_vocab = {i: t for t, i in self.vocab.items()}
        return ' '.join(rev_vocab.get(i, '<unk>') for i in tokens)

# Example
if __name__ == '__main__':
    corpus = ["míyax túpanax yawúsh", "noona míyax", "túpanax yawúsh"]
    tokenizer = LuisenoTokenizer()
    vocab = tokenizer.build_vocab(corpus)
    print("Vocabulary:", vocab)
    encoded = tokenizer.encode("míyax túpanax")
    print("Encoded:", encoded)
    print("Decoded:", tokenizer.decode(encoded))
