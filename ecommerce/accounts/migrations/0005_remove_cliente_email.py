# Generated by Django 4.1 on 2022-10-07 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_nome_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
    ]
