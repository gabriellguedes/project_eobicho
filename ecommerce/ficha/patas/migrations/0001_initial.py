# Generated by Django 4.1 on 2022-10-31 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patas', models.CharField(max_length=100, verbose_name='')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
