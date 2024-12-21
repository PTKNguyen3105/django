from django.urls import path
from . import views

urlpatterns = [
    path('Kois/', views.members, name='Kois'),
]