# apps/adminpanel/views.py

from django.shortcuts import render, redirect
from django.conf import settings
from .decorators import admin_required
from .services import (
    get_platform_stats,
    block_user,
    remove_inactive_users,
    get_system_logs,
    trigger_model_update
)
from django.contrib.auth import get_user_model

User = get_user_model()


@admin_required
def admin_dashboard_view(request):
    stats = get_platform_stats()
    users = User.objects.all()

    return render(request, 'adminpanel/dashboard.html', {
        "stats": stats,
        "users": users
    })


@admin_required
def block_user_view(request, user_id):
    block_user(user_id)
    return redirect('admin_dashboard')


@admin_required
def remove_inactive_view(request):
    count = remove_inactive_users()

    return render(request, 'adminpanel/users.html', {
        "message": f"{count} inactive users removed"
    })


@admin_required
def logs_view(request):
    logs = get_system_logs(settings.BASE_DIR / 'logs/system.log')

    return render(request, 'adminpanel/logs.html', {
        "logs": logs
    })


@admin_required
def model_update_view(request):
    message = trigger_model_update()

    return render(request, 'adminpanel/trends.html', {
        "message": message
    })