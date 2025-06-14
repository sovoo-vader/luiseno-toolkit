# SentimentAnnotator – Classify Narrative Sentiment Across Cultural Texts

from textblob import TextBlob
import re

def annotate_sentiment(text):
    sentences = re.split(r'[.!?]', text)
    results = []
    for sent in sentences:
        if sent.strip():
            polarity = TextBlob(sent).sentiment.polarity
            if polarity > 0.2:
                tag = "POSITIVE"
            elif polarity < -0.2:
                tag = "NEGATIVE"
            else:
                tag = "NEUTRAL"
            results.append((sent.strip(), tag))
    return results

# Example
if __name__ == '__main__':
    sample = "We danced under the stars. They burned our baskets. Grandfather smiled."
    for sent, tag in annotate_sentiment(sample):
        print(f"[{tag}] {sent}")
