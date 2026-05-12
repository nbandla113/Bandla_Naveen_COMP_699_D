from django import forms
from .models import Content


class TextReviewForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['text']


class ImageReviewForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['image']


class DraftReviewForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['text', 'image']