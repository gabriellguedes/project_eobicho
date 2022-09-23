# Generated by Django 4.1 on 2022-09-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0005_doenca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condicao_pelos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelosCondicao', models.CharField(max_length=100, verbose_name='Condição dos Pelos')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Estado_pelos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelosEstado', models.CharField(max_length=100, verbose_name='Estado do Pelo')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.RemoveField(
            model_name='pelos',
            name='pelosCondicao',
        ),
        migrations.RemoveField(
            model_name='pelos',
            name='pelosEstado',
        ),
    ]
