# SemanticDriftTracker – Compare Gloss Usage Over Time in Parallel Translations

import matplotlib.pyplot as plt
from collections import defaultdict

# Simulated data: year -> {gloss: count}
corpus_glosses = {
    1900: {"spirit": 10, "coyote": 14, "moon": 7},
    1950: {"spirit": 5, "coyote": 12, "moon": 10},
    2000: {"spirit": 2, "coyote": 6, "moon": 14},
    2020: {"spirit": 1, "coyote": 5, "moon": 16}
}

def plot_drift(word):
    years = sorted(corpus_glosses)
    counts = [corpus_glosses[y].get(word, 0) for y in years]
    plt.plot(years, counts, marker='o')
    plt.title(f"Semantic Drift of '{word}' over Time")
    plt.xlabel("Year")
    plt.ylabel("Frequency in Gloss")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example use
if __name__ == '__main__':
    plot_drift("spirit")
