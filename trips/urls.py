from django.urls import path
from . import views


app_name = 'trips'
urlpatterns = [
    path('', views.TripIndexView.as_view(), name='index'),
    path('<int:pk>/', views.TripDetailView.as_view(), name='detail'),
    path('new/', views.TripCreateView.as_view(), name='new'),
    path('edit/<int:pk>/', views.TripUpdateView.as_view(), name='edit'),
    path('trips/<int:pk>/star/', views.star_trip, name='star'),
    path('delete/<int:pk>/', views.delete_trip, name='delete'),
]
