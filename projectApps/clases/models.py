from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ..entrenamiento.models import UserProfile


class Location(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    trainer = models.ForeignKey(
        UserProfile, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=255, blank=False)
    frecuency_3_by_week = models.IntegerField()
    frecuency_2_by_week = models.IntegerField()

    def __str__(self):
        return self.name


class Weekday(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AvailableHour(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    day = models.ForeignKey(Weekday, on_delete=models.CASCADE)
    hour = models.CharField(max_length=5, null=False, blank=False)

    def __str__(self):
        return self.hour


class TestClass(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.IntegerField()
    class_location = models.ForeignKey(
        Location, null=False, on_delete=models.CASCADE)
    class_date = models.DateField(null=False, blank=False)
    class_hour = models.ForeignKey(
        AvailableHour, blank=False, on_delete=models.CASCADE)

    def get_weekday_name(self):
        if self.class_date:
            return self.class_date.strftime('%A')
        return None

    def save(self, *args, **kwargs):
        if self.class_date:
            self.class_day, _ = Weekday.objects.get_or_create(
                name=self.class_date.get_weekday_name())

        super(TestClass, self).save(*args, **kwargs)
