# apps/ai_engine/preprocessing.py

import re


def clean_text(text):
    """
    Basic text preprocessing
    """

    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()

    return text