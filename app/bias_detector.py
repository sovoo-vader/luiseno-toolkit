# File: app/bias_detector.py
from transformers import pipeline

classifier = pipeline("zero-shot-classification")

def detect_bias(sentence):
    labels = ["colonial bias", "neutral", "indigenous framing"]
    return classifier(sentence, labels)