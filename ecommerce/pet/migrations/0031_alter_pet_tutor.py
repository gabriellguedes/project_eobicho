# Generated by Django 4.1 on 2022-11-03 15:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet', '0030_alter_pet_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='tutor',
            field=models.ManyToManyField(related_name='tutores', to=settings.AUTH_USER_MODEL),
        ),
    ]
