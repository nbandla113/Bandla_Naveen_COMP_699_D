# -------------------------------
# CALCULATE FINAL RISK
# -------------------------------
def calculate_risk(llm_score, nlp_score, reasons=None):
    """
    Combine LLM + NLP scores and assign risk level
    Also uses detected categories for smarter decisions
    """

    # -------------------------------
    # NORMALIZE INPUT
    # -------------------------------
    llm_score = max(0, min(llm_score, 1))
    nlp_score = max(0, min(nlp_score, 1))

    # -------------------------------
    # BASE WEIGHTED SCORE
    # -------------------------------
    final_score = (llm_score * 0.6) + (nlp_score * 0.4)

    # -------------------------------
    # BOOST IF BOTH MODELS AGREE
    # -------------------------------
    if llm_score > 0.5 and nlp_score > 0.5:
        final_score += 0.1

    # -------------------------------
    # CATEGORY-BASED OVERRIDES (IMPORTANT)
    # -------------------------------
    if reasons:
        for r in reasons:

            # 🔥 SEXUAL → ALWAYS HIGH
            if "SEXUAL" in r:
                return 0.9, "High"

            # 🔥 SELF HARM → ALWAYS HIGH
            if "SELF_HARM" in r:
                return 1.0, "High"

            # 🔴 THREAT → HIGH
            if "THREAT" in r:
                final_score = max(final_score, 0.75)

            # ⚠️ HARASSMENT / ABUSE → at least MEDIUM
            if "HARASSMENT" in r or "ABUSE" in r:
                final_score = max(final_score, 0.5)

    # -------------------------------
    # FINAL NORMALIZATION
    # -------------------------------
    final_score = min(final_score, 1.0)

    # -------------------------------
    # RISK LEVEL CLASSIFICATION
    # -------------------------------
    if final_score >= 0.7:
        level = "High"
    elif final_score >= 0.4:
        level = "Medium"
    else:
        level = "Low"

    return round(final_score, 2), level