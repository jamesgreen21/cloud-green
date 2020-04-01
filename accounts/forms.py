from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """
    Returns a form regsiter form
    """
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name'
        ]


class UserUpdateForm(forms.ModelForm):
    """
    Returns a form update profile form
    """
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
