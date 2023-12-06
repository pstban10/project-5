from . import models
from django.forms import ModelForm


class ExerciseForm(ModelForm):
    class Meta:
        model = models.Exercise
        fields = [
            'exercise_name',
            'description',
            'category',
            'url_video',
        ]


class ProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
            'address',
            'weight',
            'height',
            'activity_level',
            'birth_date',
            'gender',
            'observations',
        ]
