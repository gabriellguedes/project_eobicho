# Generated by Django 4.1 on 2022-10-03 13:16

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0008_photo_remove_pet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/'), upload_to='', verbose_name='Foto do Pet'),
        ),
    ]
