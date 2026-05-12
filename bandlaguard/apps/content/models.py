from django.db import models
from django.conf import settings


class Content(models.Model):
    CONTENT_TYPE_CHOICES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('draft', 'Draft'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('discarded', 'Discarded'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)

    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content_type}"


class ReviewResult(models.Model):
    RISK_LEVEL_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    content = models.OneToOneField(Content, on_delete=models.CASCADE)

    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL_CHOICES)
    score = models.FloatField()

    reasons = models.TextField()
    suggestions = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content.id} - {self.risk_level}"