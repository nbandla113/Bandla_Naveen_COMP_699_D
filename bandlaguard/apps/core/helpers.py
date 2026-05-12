# apps/core/helpers.py

import os
from datetime import datetime


def format_datetime(dt):
    """
    Convert datetime to readable format
    """
    if not dt:
        return ""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def safe_divide(a, b):
    """
    Avoid division by zero
    """
    return a / b if b != 0 else 0


def truncate_text(text, length=100):
    """
    Shorten long text
    """
    if not text:
        return ""
    return text[:length] + "..." if len(text) > length else text


def ensure_directory(path):
    """
    Create directory if not exists
    """
    os.makedirs(path, exist_ok=True)


def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def normalize_text(text):
    """
    Basic normalization
    """
    if not text:
        return ""
    return text.strip().lower()


def calculate_percentage(part, total):
    """
    Safe percentage calculation
    """
    if total == 0:
        return 0
    return round((part / total) * 100, 2)