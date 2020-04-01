from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
)


def register(request):
    """
    Returns a view that renders the register page and form
    """
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            messages.success(request, 'Registration complete. Let the fun begin!')
    else:
        user_form = UserRegisterForm()

    context = {
        'title': 'Register',
        'nbar': 'register',
        'user_form': user_form,
    }
    return render(request, 'register.html', context)


@login_required
def profile(request):
    """
    Returns a view that renders the profile page and form
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('accounts:user')

    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'title': 'Profile',
        'nbar': 'profile',
        'user_form': user_form,
    }

    return render(request, 'profile.html', context)
