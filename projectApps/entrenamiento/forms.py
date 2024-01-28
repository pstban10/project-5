from . import models
from django.forms import ModelForm


# agrega informacion complementaria del usuario
class ProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
            'address',
            'phone',
            'weight',
            'height',
            'activity_level',
            'birth_date',
            'gender',
            'observations',
            'profile_picture',
        ]

# agrega ejercicios a la lista de ejercicios


class ExerciseForm(ModelForm):
    class Meta:
        model = models.Exercise
        fields = [
            'exercise_name',
            'description',
            'category',
            'url_video',
        ]

# Agrega rutinas para tener como predeterminadas


class RoutinesForm(ModelForm):
    class Meta:
        model = models.Routine
        fields = [
            'routine_name',
            'category',
            'level',
            'description',
        ]

# Asocia los ejercicios a las rutinas que creamos


class RoutineExerciseForm(ModelForm):
    class Meta:
        model = models.RoutineExercise
        fields = [
            'routine',
            'exercise',
            'repetitions',
            'sets',
        ]

# Agrega Rutinas creadas en el formulario anterior a los perfiles de los usuarios


class UserRoutinesForm(ModelForm):
    class Meta:
        model = models.UserRoutine
        fields = [
            'user',
            'routine',
            'start_date',
            'end_date',
        ]
