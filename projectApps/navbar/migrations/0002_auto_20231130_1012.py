# Generated by Django 3.2.16 on 2023-11-30 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rutina',
            name='Ejercicios',
        ),
        migrations.RemoveField(
            model_name='rutina',
            name='creador',
        ),
        migrations.DeleteModel(
            name='EjercicioCalistenia',
        ),
        migrations.DeleteModel(
            name='PatronMovimiento',
        ),
        migrations.DeleteModel(
            name='Rutina',
        ),
    ]