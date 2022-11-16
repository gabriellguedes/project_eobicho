# Generated by Django 4.1.3 on 2022-11-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_ficha_funcionario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha',
            name='banho',
        ),
        migrations.RemoveField(
            model_name='ficha',
            name='itens',
        ),
        migrations.RemoveField(
            model_name='ficha',
            name='tosa',
        ),
        migrations.AddField(
            model_name='ficha',
            name='banho',
            field=models.ManyToManyField(to='services.banho', verbose_name='Banho'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='itens',
            field=models.ManyToManyField(to='services.itens', verbose_name='Itens do Pet'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='tosa',
            field=models.ManyToManyField(to='services.tosa', verbose_name='Tosa'),
        ),
    ]
