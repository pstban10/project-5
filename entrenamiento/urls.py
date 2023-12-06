from django.urls import path
from . import views


urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
    path('edit_perfil/', views.edit_perfil, name='edit_perfil'),
    path('rutinas/', views.rutinas, name='rutinas'),
    path('ejercicios/', views.ejercicios, name='ejercicios'),
    path('addex/', views.aggejercicio, name='addex'),


]
