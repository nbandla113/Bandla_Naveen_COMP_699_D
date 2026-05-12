# apps/reports/services.py

from apps.content.models import Content, ReviewResult
from .models import Report


def generate_user_summary(user):
    contents = Content.objects.filter(user=user)
    total = contents.count()

    low = ReviewResult.objects.filter(content__user=user, risk_level='low').count()
    medium = ReviewResult.objects.filter(content__user=user, risk_level='medium').count()
    high = ReviewResult.objects.filter(content__user=user, risk_level='high').count()

    summary = {
        "total_reviews": total,
        "low_risk": low,
        "medium_risk": medium,
        "high_risk": high
    }

    return summary


def generate_platform_trends():
    total = ReviewResult.objects.count()

    low = ReviewResult.objects.filter(risk_level='low').count()
    medium = ReviewResult.objects.filter(risk_level='medium').count()
    high = ReviewResult.objects.filter(risk_level='high').count()

    trends = {
        "total_reviews": total,
        "low": low,
        "medium": medium,
        "high": high
    }

    return trends


def save_report(report_type, data):
    report = Report.objects.create(
        report_type=report_type,
        data_snapshot=str(data)
    )
    return report