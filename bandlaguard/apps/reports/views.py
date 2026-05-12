# apps/reports/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import generate_user_summary, generate_platform_trends, save_report
from .exporters import export_to_file


@login_required
def user_summary_view(request):
    summary = generate_user_summary(request.user)

    report = save_report("summary", summary)
    file_path = export_to_file(report)

    return render(request, 'reports/export.html', {
        "data": summary,
        "file": file_path
    })


@login_required
def platform_trend_view(request):
    trends = generate_platform_trends()

    report = save_report("trend", trends)
    file_path = export_to_file(report)

    return render(request, 'reports/export.html', {
        "data": trends,
        "file": file_path
    })