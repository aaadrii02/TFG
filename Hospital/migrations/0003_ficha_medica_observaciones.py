# Generated by Django 4.1.4 on 2023-05-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_cita_dni_medico'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha_medica',
            name='observaciones',
            field=models.CharField(default='', max_length=10000),
        ),
    ]