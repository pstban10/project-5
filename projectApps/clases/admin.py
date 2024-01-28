from django.contrib import admin
from .models import TestClass, Location, Weekday, AvailableHour

# Register your models here.
admin.site.register(Location)
admin.site.register(Weekday)
admin.site.register(AvailableHour)
admin.site.register(TestClass)
