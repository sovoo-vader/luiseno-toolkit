# WordFrequencyVisualizer – Generate Heatmap of Morpheme Usage Frequency

import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
import re

sns.set(style="whitegrid")

def clean_and_tokenize(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    return text.split()

def plot_frequency(text):
    tokens = clean_and_tokenize(text)
    counts = Counter(tokens).most_common(15)
    words, freqs = zip(*counts)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(freqs), y=list(words), palette="mako")
    plt.title("Top 15 Morphemes or Words")
    plt.xlabel("Frequency")
    plt.ylabel("Morpheme")
    plt.tight_layout()
    plt.show()

# Example use
if __name__ == '__main__':
    sample_text = "míyax túpanax míyax yawúsh yawúsh túpanax noona míyax"
    plot_frequency(sample_text)
