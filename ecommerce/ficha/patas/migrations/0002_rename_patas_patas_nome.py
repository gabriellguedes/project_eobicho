# Generated by Django 4.1 on 2022-11-05 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patas',
            old_name='patas',
            new_name='nome',
        ),
    ]