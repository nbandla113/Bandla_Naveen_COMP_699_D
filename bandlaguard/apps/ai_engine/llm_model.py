import re

# -------------------------------
# CLEAN TEXT
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# -------------------------------
# HIGH RISK PATTERNS
# -------------------------------
HIGH_RISK_PATTERNS = [

    #  THREATS
    r"\bi will kill you\b",
    r"\byou should die\b",
    r"\bgo die\b",
    r"\bi will hurt you\b",
    r"\bi will destroy you\b",

    #  STRONG ABUSE
    r"\byou are a bitch\b",
    r"\byou are stupid\b",
    r"\byou are an idiot\b",
    r"\byou are useless\b",
    r"\byou are trash\b",
    r"\byou are worthless\b",

    #  SEXUAL (VERY IMPORTANT)
    r"\bsend\s+(me\s+)?nudes\b",
    r"\bnude(s)?\b",
    r"\bsex\b",
    r"\bporn\b",
    r"\bxxx\b",
    r"\bshow\s+(me\s+)?your\s+body\b",
    r"\bi want sex\b",
    r"\blets have sex\b",
    r"\byou are sexy\b",
    r"\bexplicit\b",

    #  HARASSMENT
    r"\bnobody likes you\b",
    r"\byou are nothing\b",
    r"\byou dont belong\b",
    r"\bgo away\b",

    #  SELF HARM
    r"\bi want to die\b",
    r"\bkill myself\b",
    r"\bend my life\b"
]


# -------------------------------
# MEDIUM RISK PATTERNS
# -------------------------------
MEDIUM_RISK_PATTERNS = [
    r"\bshut up\b",
    r"\bleave me alone\b",
    r"\byou are annoying\b",
    r"\bthis is bad\b",
    r"\byou are dumb\b",
    r"\bthis is stupid\b"
]


# -------------------------------
# NEGATIVE WORDS
# -------------------------------
NEGATIVE_WORDS = [
    "bitch", "idiot", "stupid", "loser", "hate",
    "dumb", "ugly", "fool", "trash", "useless",
    "annoying", "bad", "worst"
]


# -------------------------------
# ANALYZE TEXT
# -------------------------------
def analyze_text_llm(text):

    cleaned = clean_text(text)

    score = 0
    detected = set()

    # -------------------------------
    # HIGH RISK DETECTION
    # -------------------------------
    for pattern in HIGH_RISK_PATTERNS:
        if re.search(pattern, cleaned):
            score += 0.7
            detected.add(pattern)

    # -------------------------------
    # MEDIUM RISK DETECTION
    # -------------------------------
    for pattern in MEDIUM_RISK_PATTERNS:
        if re.search(pattern, cleaned):
            score += 0.3
            detected.add(pattern)

    # -------------------------------
    # WORD-LEVEL DETECTION
    # -------------------------------
    words = cleaned.split()
    negative_count = 0

    for word in words:
        if word in NEGATIVE_WORDS:
            negative_count += 1
            detected.add(word)

    score += min(negative_count * 0.1, 0.5)

    # -------------------------------
    # STRONG BOOSTS
    # -------------------------------
    if negative_count >= 2:
        score += 0.2

    if len(detected) >= 3:
        score += 0.2

    #  FORCE HIGH IF SEXUAL KEYWORD FOUND
    if re.search(r"\bnude|sex|porn|xxx\b", cleaned):
        score = max(score, 0.8)

    # -------------------------------
    # NORMALIZE
    # -------------------------------
    score = min(score, 1.0)

    return round(score, 2)