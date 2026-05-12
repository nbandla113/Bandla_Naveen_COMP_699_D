# apps/ai_engine/suggestion_engine.py

def generate_suggestions(reasons):
    """
    Generate smart suggestions based on detected categories
    """

    # -------------------------------
    # SAFE CASE
    # -------------------------------
    if not reasons or "No harmful content detected" in reasons:
        return ["Your content looks safe"]

    suggestions = set()  # avoid duplicates

    # -------------------------------
    # CATEGORY-BASED SUGGESTIONS
    # -------------------------------
    for reason in reasons:

        reason_upper = reason.upper()

        # 🔴 THREAT
        if "THREAT" in reason_upper:
            suggestions.add("Avoid using threatening or violent language")

        # 🔴 ABUSE
        if "ABUSE" in reason_upper:
            suggestions.add("Avoid insulting or offensive words")

        # 🔴 HATE
        if "HATE" in reason_upper:
            suggestions.add("Avoid discriminatory or hateful language")

        # 🔥 SEXUAL
        if "SEXUAL" in reason_upper:
            suggestions.add("Avoid explicit or inappropriate sexual content")

        # 🔥 HARASSMENT
        if "HARASSMENT" in reason_upper:
            suggestions.add("Avoid bullying or harassing language")

        # 🔥 SELF HARM
        if "SELF_HARM" in reason_upper:
            suggestions.add("Please seek support and avoid self-harm related content")

    # -------------------------------
    # GENERIC IMPROVEMENT SUGGESTIONS
    # -------------------------------
    suggestions.add("Use respectful and professional language")
    suggestions.add("Think before posting to ensure your message is appropriate")

    return list(suggestions)