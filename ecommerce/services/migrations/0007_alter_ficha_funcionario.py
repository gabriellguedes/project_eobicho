# Generated by Django 4.1.3 on 2022-11-14 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0006_alter_ficha_outros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='funcionario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]