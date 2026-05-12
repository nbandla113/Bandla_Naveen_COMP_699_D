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
# HARMFUL PATTERNS (REGEX BASED)
# -------------------------------
HARMFUL_PATTERNS = {

    # 🔴 THREATS
    "threat": [
        r"\bkill\b", r"\bmurder\b", r"\battack\b", r"\bhurt\b",
        r"\bi will kill you\b", r"\byou should die\b",
        r"\bend you\b", r"\bcrush you\b"
    ],

    # 🔴 ABUSE
    "abuse": [
        r"\bidiot\b", r"\bstupid\b", r"\bloser\b", r"\bdumb\b",
        r"\bbitch\b", r"\bfool\b", r"\btrash\b",
        r"\buseless\b", r"\bworthless\b", r"\bugly\b"
    ],

    # 🔴 HATE / DISCRIMINATION
    "hate": [
        r"\brace\b", r"\bracist\b", r"\bsexist\b",
        r"\bgo back\b", r"\bnot welcome\b",
        r"\binferior\b", r"\bsuperior\b"
    ],

    # 🔥 SEXUAL (IMPORTANT FIX)
    "sexual": [
        r"\bsend\s+(me\s+)?nudes\b",
        r"\bnude(s)?\b",
        r"\bsex\b",
        r"\bporn\b",
        r"\bxxx\b",
        r"\bnaked\b",
        r"\bshow\s+(me\s+)?your\s+body\b",
        r"\bexplicit\b",
        r"\bsexy\b",
        r"\bfuck\b"
    ],

    # 🔥 HARASSMENT
    "harassment": [
        r"\bshut up\b",
        r"\bgo away\b",
        r"\bleave me alone\b",
        r"\bnobody likes you\b",
        r"\byou are nothing\b",
        r"\byou are worthless\b",
        r"\byou dont belong\b"
    ],

    # 🔥 SELF-HARM
    "self_harm": [
        r"\bkill myself\b",
        r"\bsuicide\b",
        r"\bend my life\b",
        r"\bi want to die\b"
    ]
}


# -------------------------------
# CATEGORY WEIGHTS
# -------------------------------
CATEGORY_WEIGHTS = {
    "threat": 0.8,
    "abuse": 0.5,
    "hate": 0.6,
    "sexual": 0.9,       # 🔥 make sexual very strong
    "harassment": 0.5,
    "self_harm": 1.0
}


# -------------------------------
# DETECT HARMFUL TEXT
# -------------------------------
def check_harmful_text(text):

    cleaned = clean_text(text)

    score = 0
    reasons = []
    detected = set()

    # -------------------------------
    # PATTERN MATCHING
    # -------------------------------
    for category, patterns in HARMFUL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, cleaned):

                if pattern not in detected:
                    detected.add(pattern)

                    score += CATEGORY_WEIGHTS.get(category, 0.3)

                    reasons.append(f"{category.upper()} detected")

    # -------------------------------
    # INTENSITY BOOST
    # -------------------------------
    if len(detected) >= 2:
        score += 0.2

    if len(detected) >= 4:
        score += 0.3

    # -------------------------------
    # FORCE HIGH FOR SEXUAL / SELF-HARM
    # -------------------------------
    for reason in reasons:
        if "SEXUAL" in reason or "SELF_HARM" in reason:
            score = max(score, 0.9)

    # -------------------------------
    # NORMALIZE
    # -------------------------------
    score = min(score, 1.0)

    return round(score, 2), reasons