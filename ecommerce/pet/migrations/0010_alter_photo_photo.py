# Generated by Django 4.1 on 2022-10-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0009_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto do Pet'),
        ),
    ]