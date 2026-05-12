from django.contrib.auth import authenticate, login, logout
from .models import User


def register_user(form):
    if form.is_valid():
        user = form.save()
        return user
    return None


def login_user(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user:
        if user.is_blocked:
            return None, "Account is blocked by admin"
        login(request, user)
        return user, None
    return None, "Invalid credentials"


def logout_user(request):
    logout(request)


def update_profile(user, form):
    if form.is_valid():
        form.save()
        return True
    return False