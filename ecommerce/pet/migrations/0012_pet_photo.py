# Generated by Django 4.1 on 2022-10-03 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0011_alter_photo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pet.photo'),
        ),
    ]