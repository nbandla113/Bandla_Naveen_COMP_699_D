# apps/shared_space/models.py

from django.db import models
from django.conf import settings


class SharedSpace(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rules = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SharedSpaceMember(models.Model):
    space = models.ForeignKey(SharedSpace, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.space.name}"


class Invitation(models.Model):
    space = models.ForeignKey(SharedSpace, on_delete=models.CASCADE)
    invited_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10,
        choices=(('pending', 'Pending'), ('accepted', 'Accepted')),
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invite to {self.invited_user.username}"