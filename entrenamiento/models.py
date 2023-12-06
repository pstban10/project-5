from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Sedentario (little or no exercise)'),
        ('Poca_actividad', 'Ligeramente activo (light exercise/sports 1-3 days/week)'),
        ('Actividad_moderada',
         'Moderadamente activo (moderate exercise/sports 3-5 days/week)'),
        ('very_active', 'Muy activo (hard exercise/sports 6-7 days a week)'),
    ]
    GENDER_CHOISES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    registration_date = models.DateField(auto_now_add=True)
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True)
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True)
    activity_level = models.CharField(
        max_length=20,
        choices=ACTIVITY_LEVEL_CHOICES,
        null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOISES,
        null=True,
        blank=True)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    url_video = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.exercise_name


class Routine(models.Model):
    routine_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.routine_name


class RoutineExercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    sets = models.IntegerField()

    class Meta:
        unique_together = ('routine', 'exercise')


class UserRoutine(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'routine', 'start_date')
