# Generated by Django 4.1.3 on 2022-11-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_remove_ficha_banho_remove_ficha_itens_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='outros',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Outros Itens'),
        ),
    ]