# Generated by Django 4.1.3 on 2022-11-14 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0014_remove_anamnese_ficha'),
        ('services', '0003_remove_ficha_anamnese'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='anamnese',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ficha.anamnese'),
            preserve_default=False,
        ),
    ]
