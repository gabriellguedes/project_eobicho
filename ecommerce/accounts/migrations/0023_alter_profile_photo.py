# Generated by Django 4.1.3 on 2022-11-21 19:52

from django.db import migrations, models
import ecommerce.accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_profile_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=ecommerce.accounts.models.upload_image_formater, verbose_name=''),
        ),
    ]
