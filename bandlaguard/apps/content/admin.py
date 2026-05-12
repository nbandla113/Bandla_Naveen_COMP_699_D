from django.contrib import admin
from .models import Content, ReviewResult


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content_type', 'status', 'created_at')
    list_filter = ('content_type', 'status')
    search_fields = ('user__username',)


@admin.register(ReviewResult)
class ReviewResultAdmin(admin.ModelAdmin):
    list_display = ('content', 'risk_level', 'score')
    list_filter = ('risk_level',)