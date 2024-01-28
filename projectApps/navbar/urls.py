
from django.urls import include, path
from . import views

urlpatterns = [
    path('2', views.inicio, name='inicio2'),
    path('', views.init, name='inicio'),
    path('b/', views.navegando, name='navegando'),
    path('login/', views.acceder, name='login'),
    path('registro/', views.registro, name='registro'),
    path('salir/', views.salir, name='salir'),
]
