# Generated by Django 3.2.16 on 2024-01-18 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entrenamiento', '0005_auto_20240114_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('frecuency_3_by_week', models.IntegerField()),
                ('frecuency_2_by_week', models.IntegerField()),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrenamiento.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('class_date', models.DateField()),
                ('class_hour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clases.availablehour')),
                ('class_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clases.location')),
            ],
        ),
        migrations.AddField(
            model_name='availablehour',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clases.weekday'),
        ),
        migrations.AddField(
            model_name='availablehour',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clases.location'),
        ),
    ]