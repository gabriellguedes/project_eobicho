# Generated by Django 4.1 on 2022-10-03 14:46

from django.db import migrations, models
import ecommerce.pet.models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0012_pet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=ecommerce.pet.models.upload_image_formater, verbose_name='Foto do Pet'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
