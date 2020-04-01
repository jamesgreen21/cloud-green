from django.shortcuts import render
from django.contrib import messages


def index(request):
    """
    Create a view of the site landing page
    """
    context = {
        'title': 'Home',
        'nbar': 'home',
    }
    messages.success(request, 'This is a test message')
    return render(request, 'main/index.html', context)
