from . import views
from django.urls import path

urlpatterns = [
    path('reserva', views.testClass, name='reserva'),
    path('calendar', views.calendar, name='calendar'),
    path('reservar/', views.get_locations, name='reservar'),
    path('horarios/<int:location_id>/<int:weekday_id>',
         views.get_hours, name='reservar'),



]
