# Generated by Django 4.1 on 2022-11-10 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0009_alter_ficha_doenca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha',
            name='peleInfeccionada',
        ),
    ]
