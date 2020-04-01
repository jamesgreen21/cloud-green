from django.urls import path, include
from django.contrib.auth import views
from accounts import views as accounts_views


app_name = 'accounts'
urlpatterns = [
    path('register/', accounts_views.register, name='register'),
    path('profile/', accounts_views.profile, name='profile'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
