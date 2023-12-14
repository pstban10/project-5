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
    path('rutinas/', views.rutinas, name='rutinas'),
    path('addRut/', views.aggRutina, name='addRut'),
    path('addRut/Exercises/<int:id>/', views.aggRutExer, name='addRutExer'),
    path('rutina/<int:id>/', views.rutina, name='rutina'),
    path('addAgenda/', views.addAgenda, name='addAgenda'),
]
