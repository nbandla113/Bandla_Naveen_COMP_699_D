# apps/core/permissions.py


def is_admin(user):
    """
    Check if user is admin
    """
    return user.is_authenticated and user.is_staff


def is_active_user(user):
    """
    Check if user is active and not blocked
    """
    if not user.is_authenticated:
        return False

    if hasattr(user, 'is_blocked') and user.is_blocked:
        return False

    return user.is_active


def can_modify_content(user, content):
    """
    Check if user can edit/delete content
    """
    return user.is_authenticated and content.user == user


def can_manage_space(user, space):
    """
    Only owner can manage shared space
    """
    return user.is_authenticated and space.owner == user


def can_view_admin_panel(user):
    """
    Only admin users allowed
    """
    return is_admin(user)