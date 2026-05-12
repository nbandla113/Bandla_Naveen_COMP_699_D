from django.urls import path
from .views import (
    text_review_view,
    image_review_view,
    draft_review_view,
    result_view,
    history_view,
    clear_history_view
)

urlpatterns = [
    path('text/', text_review_view, name='text_review'),
    path('image/', image_review_view, name='image_review'),
    path('draft/', draft_review_view, name='draft_review'),
    path('result/<int:content_id>/', result_view, name='result'),
    path('history/', history_view, name='history'),
    path('clear-history/', clear_history_view, name='clear_history'),
]