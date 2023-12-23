from . import views
from django.urls import path

urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),

]
