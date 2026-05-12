from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, ProfileForm
from .services import register_user, login_user, logout_user, update_profile


def register_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        user = register_user(form)
        if user:
            return redirect('login')

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")

        user, error = login_user(request, username, password)
        if user:
            return redirect('dashboard')

        return render(request, "accounts/login.html", {
            "form": form,
            "error": error
        })

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout_user(request)
    return redirect('login')


@login_required
def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")


@login_required
def profile_view(request):
    form = ProfileForm(instance=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if update_profile(request.user, form):
            return redirect('dashboard')

    return render(request, "accounts/profile.html", {"form": form})