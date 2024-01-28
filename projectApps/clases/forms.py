from django import forms
from . import models
from django.forms import ModelForm


class TestClassForm(ModelForm):
    class Meta:
        model = models.TestClass
        fields = [
            'full_name',
            'phone',
            'class_location',
            'class_date',
            'class_hour'
        ]

        widgets = {
            'class_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        class_location = cleaned_data.get('class_location')
        class_date = cleaned_data.get('class_date')
        class_hour = cleaned_data.get('class_hour')

        if class_date and not class_location.availablehour_set.filter(day__name=class_date.get_weekday_name()).exists():
            raise forms.ValidationError(
                {'class_hour': 'No hay horarios disponibles para este día y locación.'})

        return cleaned_data
