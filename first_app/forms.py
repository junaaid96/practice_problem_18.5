from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=100, required=True)
    last_name=forms.CharField(max_length=100, required=True)
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email')

class EditProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email')
