# Generated by Django 3.2.16 on 2023-12-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamiento', '0005_alter_exercise_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
