from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# =========================
# REGISTER FORM
# =========================
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': '',  # uses your global CSS
                'placeholder': field.label,
            })


# =========================
# LOGIN FORM
# =========================
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })

        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password'
        })


# =========================
# PROFILE FORM
# =========================
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'placeholder': field.label
            })