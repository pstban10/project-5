# Generated by Django 3.2.16 on 2023-12-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamiento', '0002_alter_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]