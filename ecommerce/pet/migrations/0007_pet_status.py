# Generated by Django 4.1 on 2022-09-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_pet_especie_pet_raca'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
