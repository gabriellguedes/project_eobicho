# Generated by Django 4.1 on 2022-11-11 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0031_alter_pet_tutor'),
        ('peso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peso',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_peso', to='pet.pet'),
        ),
    ]
