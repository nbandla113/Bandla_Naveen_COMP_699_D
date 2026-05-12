# apps/shared_space/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateSpaceForm, JoinSpaceForm, InviteUserForm
from .services import (
    create_space, join_space, exit_space,
    invite_user, get_user_spaces, get_space_members
)
from .models import SharedSpace


@login_required
def create_space_view(request):
    form = CreateSpaceForm()

    if request.method == "POST":
        form = CreateSpaceForm(request.POST)
        if form.is_valid():
            create_space(
                request.user,
                form.cleaned_data['name'],
                form.cleaned_data['rules']
            )
            return redirect('dashboard')

    return render(request, 'shared/create_space.html', {'form': form})


@login_required
def join_space_view(request):
    form = JoinSpaceForm()

    if request.method == "POST":
        form = JoinSpaceForm(request.POST)
        if form.is_valid():
            join_space(request.user, form.cleaned_data['space_id'])
            return redirect('dashboard')

    return render(request, 'shared/join_space.html', {'form': form})


@login_required
def exit_space_view(request, space_id):
    exit_space(request.user, space_id)
    return redirect('dashboard')


@login_required
def manage_space_view(request, space_id):
    space = SharedSpace.objects.get(id=space_id)
    members = get_space_members(space)

    form = InviteUserForm()

    if request.method == "POST":
        form = InviteUserForm(request.POST)
        if form.is_valid():
            invite_user(space, form.cleaned_data['username'])

    return render(request, 'shared/manage_space.html', {
        'space': space,
        'members': members,
        'form': form
    })


@login_required
def user_spaces_view(request):
    spaces = get_user_spaces(request.user)
    return render(request, 'shared/group_activity.html', {'spaces': spaces})