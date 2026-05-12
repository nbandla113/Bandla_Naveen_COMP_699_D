# apps/reports/models.py

from django.db import models


class Report(models.Model):
    REPORT_TYPE_CHOICES = (
        ('summary', 'User Summary'),
        ('trend', 'Platform Trend'),
    )

    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)

    generated_at = models.DateTimeField(auto_now_add=True)
    file_path = models.FileField(upload_to='reports/', blank=True, null=True)

    data_snapshot = models.TextField()  # store summary data

    def __str__(self):
        return f"{self.report_type} - {self.generated_at}"