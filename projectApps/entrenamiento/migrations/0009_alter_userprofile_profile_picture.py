# Generated by Django 3.2.16 on 2023-12-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamiento', '0008_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='imgs\\profile_pics'),
        ),
    ]
