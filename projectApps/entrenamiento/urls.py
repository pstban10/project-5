from django.urls import path
from . import views


urlpatterns = [
    # PERFIL
    path('perfil/', views.perfil, name='perfil'),
    path('edit_perfil/', views.edit_perfil, name='edit_perfil'),
    # EJERCICIOS
    path('ejercicios/', views.Ejercicios.as_view(), name='ejercicios'),
    path('addex/', views.aggejercicio, name='addex'),
    # RUTINAS
    path('RutinasList', views.RutinasList.as_view(), name='RutinasList'),
    path('RutinasCreator', views.RutinasCreator.as_view(), name='RutinasCreator'),
    path('RutinaEditor/<int:id>/',
         views.RutinaEditor.as_view(), name='RutinaEditor'),
    path('newRutina', views.newRut, name='newRutina'),
    path('putRut/', views.putRut, name='putRut'),
    path('rutina/<int:id>/', views.rutina, name='rutina'),

]
