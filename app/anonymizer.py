# File: app/anonymizer.py
import re

def anonymize_text(text):
    return re.sub(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b', '[REDACTED]', text)
