# Generated by Django 4.1 on 2022-11-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doenca', '0001_initial'),
        ('ficha', '0008_remove_ficha_boca_remove_ficha_doenca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='doenca',
            field=models.ManyToManyField(related_name='doencas_geral', to='doenca.doenca'),
        ),
    ]
