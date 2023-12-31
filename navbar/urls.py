"""lcalistenics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('perfil/', views.perfil, name='perfil'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.acceder, name='login'),
    path('ubicaciones/', views.ubicaciones, name='ubicaciones'),
    path('rutinas/', views.rutinas, name='rutinas'),
    path('registro/', views.registro, name='registro'),
    path('salir/', views.salir, name='salir'),

]
