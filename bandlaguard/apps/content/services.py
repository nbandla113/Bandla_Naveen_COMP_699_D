import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Content, ReviewResult

# ✅ FIXED IMPORTS (IMPORTANT)
from apps.ai_engine.llm_model import analyze_text_llm
from apps.ai_engine.nlp_model import check_harmful_text
from apps.ai_engine.cnn_model import analyze_image_cnn
from apps.ai_engine.risk_engine import calculate_risk
from apps.ai_engine.suggestion_engine import generate_suggestions


# -------------------------------
# TEXT REVIEW
# -------------------------------
def process_text_review(user, text):
    content = Content.objects.create(
        user=user,
        content_type='text',
        text=text
    )

    llm_score = analyze_text_llm(text)
    nlp_score, reasons = check_harmful_text(text)

    risk_score, risk_level = calculate_risk(llm_score, nlp_score)

    # ✅ correct usage
    suggestions = generate_suggestions(reasons)

    ReviewResult.objects.create(
        content=content,
        risk_level=risk_level,
        score=risk_score,
        reasons="\n".join(reasons),
        suggestions="\n".join(suggestions)
    )

    return content


# -------------------------------
# IMAGE REVIEW
# -------------------------------
def process_image_review(user, image):
    content = Content.objects.create(
        user=user,
        content_type='image',
        image=image
    )

    # ✅ SAVE IMAGE
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
    filename = fs.save(image.name, image)
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    # ✅ ANALYZE IMAGE
    image_score, reasons = analyze_image_cnn(file_path)

    risk_score, risk_level = calculate_risk(image_score, image_score)

    suggestions = ["Avoid sharing harmful or sensitive visuals"]

    ReviewResult.objects.create(
        content=content,
        risk_level=risk_level,
        score=risk_score,
        reasons="\n".join(reasons),
        suggestions="\n".join(suggestions)
    )

    return content


# -------------------------------
# DRAFT REVIEW (TEXT + IMAGE)
# -------------------------------
def process_draft_review(user, text, image):
    content = Content.objects.create(
        user=user,
        content_type='draft',
        text=text,
        image=image
    )

    # TEXT ANALYSIS
    llm_score = analyze_text_llm(text)
    nlp_score, reasons_text = check_harmful_text(text)

    # IMAGE ANALYSIS
    image_score, reasons_image = (0, [])

    if image:
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(image.name, image)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        image_score, reasons_image = analyze_image_cnn(file_path)

    # COMBINE SCORES
    combined_llm = (llm_score + image_score) / 2
    final_score, risk_level = calculate_risk(combined_llm, nlp_score)

    reasons = reasons_text + reasons_image

    suggestions = generate_suggestions(reasons)

    ReviewResult.objects.create(
        content=content,
        risk_level=risk_level,
        score=final_score,
        reasons="\n".join(reasons),
        suggestions="\n".join(suggestions)
    )

    return content


# -------------------------------
# GET RESULT
# -------------------------------
def get_review_result(content):
    return ReviewResult.objects.get(content=content)


# -------------------------------
# USER HISTORY
# -------------------------------
def get_user_history(user):
    return Content.objects.filter(user=user).order_by('-created_at')


# -------------------------------
# CLEAR HISTORY
# -------------------------------
def clear_history(user):
    Content.objects.filter(user=user).delete()