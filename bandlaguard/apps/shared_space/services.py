# apps/shared_space/services.py

from .models import SharedSpace, SharedSpaceMember, Invitation
from django.contrib.auth import get_user_model

User = get_user_model()


def create_space(user, name, rules):
    space = SharedSpace.objects.create(
        owner=user,
        name=name,
        rules=rules
    )

    SharedSpaceMember.objects.create(space=space, user=user)
    return space


def join_space(user, space_id):
    try:
        space = SharedSpace.objects.get(id=space_id)
        SharedSpaceMember.objects.get_or_create(space=space, user=user)
        return True
    except:
        return False


def exit_space(user, space_id):
    try:
        membership = SharedSpaceMember.objects.get(space_id=space_id, user=user)
        membership.delete()
        return True
    except:
        return False


def invite_user(space, username):
    try:
        user = User.objects.get(username=username)
        Invitation.objects.create(space=space, invited_user=user)
        return True
    except:
        return False


def accept_invitation(user, space_id):
    try:
        invitation = Invitation.objects.get(space_id=space_id, invited_user=user)
        invitation.status = 'accepted'
        invitation.save()

        SharedSpaceMember.objects.get_or_create(space_id=space_id, user=user)
        return True
    except:
        return False


def remove_member(space, user_id):
    try:
        member = SharedSpaceMember.objects.get(space=space, user_id=user_id)
        member.delete()
        return True
    except:
        return False


def get_user_spaces(user):
    return SharedSpaceMember.objects.filter(user=user)


def get_space_members(space):
    return SharedSpaceMember.objects.filter(space=space)