# apps/shared_space/forms.py

from django import forms
from .models import SharedSpace


class CreateSpaceForm(forms.ModelForm):
    class Meta:
        model = SharedSpace
        fields = ['name', 'rules']


class JoinSpaceForm(forms.Form):
    space_id = forms.IntegerField(label="Enter Space ID")


class InviteUserForm(forms.Form):
    username = forms.CharField(label="Username to invite")