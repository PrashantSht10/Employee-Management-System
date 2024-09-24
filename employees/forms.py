from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username', 'class': 'textfield'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email', 'class': 'textfield'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password', 'class': 'textfield'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password', 'class': 'textfield'})


class LoginForm(forms.Form):
    """Form for user login."""
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
