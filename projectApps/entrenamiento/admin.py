from django.contrib import admin
from .models import Exercise, Routine, RoutineExercise, UserProfile, UserRoutine
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Exercise)
admin.site.register(Routine)
admin.site.register(RoutineExercise)
admin.site.register(UserRoutine)
