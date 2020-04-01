from django.shortcuts import render


def index(request):
    """
    Create a view of the site landing page
    """
    context = {
        'title': 'Home',
        'nbar': 'home',
    }
    return render(request, 'main/index.html', context)
