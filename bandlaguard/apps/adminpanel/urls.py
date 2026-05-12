# apps/adminpanel/urls.py

from django.urls import path
from .views import (
    admin_dashboard_view,
    block_user_view,
    remove_inactive_view,
    logs_view,
    model_update_view
)

urlpatterns = [
    path('', admin_dashboard_view, name='admin_dashboard'),
    path('block/<int:user_id>/', block_user_view, name='block_user'),
    path('remove-inactive/', remove_inactive_view, name='remove_inactive'),
    path('logs/', logs_view, name='view_logs'),
    path('model-update/', model_update_view, name='model_update'),
]