# Generated by Django 4.1 on 2022-11-05 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pelos', '0002_coloracao_pelagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coloracao',
            old_name='coloracao',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='condicao_pelos',
            old_name='pelosCondicao',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='estado_pelos',
            old_name='pelosEstado',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='pelagem',
            old_name='pelagem',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='pelos',
            old_name='pelos',
            new_name='nome',
        ),
    ]
