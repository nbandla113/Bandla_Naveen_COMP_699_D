# apps/shared_space/admin.py

from django.contrib import admin
from .models import SharedSpace, SharedSpaceMember, Invitation


@admin.register(SharedSpace)
class SharedSpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')


@admin.register(SharedSpaceMember)
class SharedSpaceMemberAdmin(admin.ModelAdmin):
    list_display = ('space', 'user', 'joined_at')


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('space', 'invited_user', 'status')