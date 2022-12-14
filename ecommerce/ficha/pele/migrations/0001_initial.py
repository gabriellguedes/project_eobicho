# Generated by Django 4.1 on 2022-10-31 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ectoparasitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ectoparasitas', models.CharField(max_length=100, verbose_name='Ectoparasitas')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Infec_pele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peleInfeccionada', models.CharField(max_length=100, verbose_name='Infecção na Pele')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Pele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pele', models.CharField(max_length=100, verbose_name='Outros')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
