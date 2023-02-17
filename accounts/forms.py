from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from allauth.account.forms import LoginForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].widget = forms.TextInput(
            attrs={
                "type": "email",
                "placeholder": "E-MAIL",
                "autocomplete": "email",
                "class": "form-control",
            }
        )
        self.fields["login"].label = ""
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "PASSWORD",
                "class": "form-control",
            }
        )
        self.fields["password"].label = ""
