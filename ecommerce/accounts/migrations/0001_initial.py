# Generated by Django 4.1 on 2022-09-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cpf', models.IntegerField(max_length=11, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telefone', models.IntegerField(max_length=11, verbose_name='Telefone')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
