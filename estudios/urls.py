from django.urls import path
from . import views

urlpatterns = [
    path('', views.estudios, name='estudios'),
]
