# Generated by Django 4.1 on 2022-10-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_cliente_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Telefone'),
        ),
    ]
