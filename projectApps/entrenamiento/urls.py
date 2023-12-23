from django.urls import path
from . import views


urlpatterns = [
    # PERFIL
    path('perfil/', views.perfil, name='perfil'),
    path('edit_perfil/', views.edit_perfil, name='edit_perfil'),
    # EJERCICIOS
    path('ejercicios/', views.ejercicios, name='ejercicios'),
    path('addex/', views.aggejercicio, name='addex'),
    # RUTINAS
    path('Rutinas/', views.Rutinas.as_view(), name='Rutinas'),
    path('Rutinas/<int:id>/', views.getRut, name='Rutinas'),
    path('aggRut', views.aggRut, name='aggRut'),
    path('addRut/Exercises/<int:id>/', views.aggRutExer, name='addRutExer'),
]
