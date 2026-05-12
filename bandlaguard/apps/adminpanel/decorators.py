# apps/adminpanel/decorators.py

from django.shortcuts import redirect


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return redirect('login')

        if not user.is_staff:
            return redirect('dashboard')

        return view_func(request, *args, **kwargs)

    return wrapper