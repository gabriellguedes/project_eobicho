# Generated by Django 4.1 on 2022-10-31 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0023_alter_peso_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peso',
            name='pet',
        ),
        migrations.RemoveField(
            model_name='peso',
            name='user',
        ),
        migrations.RemoveField(
            model_name='raca',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='raca',
        ),
        migrations.DeleteModel(
            name='Especie',
        ),
        migrations.DeleteModel(
            name='Peso',
        ),
        migrations.DeleteModel(
            name='Raca',
        ),
    ]
