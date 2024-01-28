# Generated by Django 3.2.16 on 2024-01-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamiento', '0003_testclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testclass',
            name='class_hour',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='testclass',
            name='class_location',
            field=models.CharField(blank=True, choices=[('GYM Belgrano', 'Gimnasio especializado Belgrano'), ('PRK Centenario', 'Parque Centenario'), ('PRK Chacabuco', 'Parque Chacabuco'), ('PRK Las Heras', 'Parque las Heras'), ('PRK Avellaneda', 'Parque Avellaneda'), ('PRK Los Andes', 'Parque los Andes'), ('PRK Irlanda', 'Plaza Irlanda')], max_length=50, null=True),
        ),
    ]