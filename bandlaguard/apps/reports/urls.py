# apps/reports/urls.py

from django.urls import path
from .views import user_summary_view, platform_trend_view

urlpatterns = [
    path('summary/', user_summary_view, name='user_summary'),
    path('trends/', platform_trend_view, name='platform_trends'),
]