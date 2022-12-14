# Generated by Django 4.1 on 2022-10-31 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0024_remove_peso_pet_remove_peso_user_remove_raca_especie_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ficha', '0003_alter_ficha_boca_alter_ficha_doenca_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristicas_Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porte', models.CharField(choices=[('Pequeno', 'Pequeno'), ('Medio', 'Médio'), ('Grande', 'Grande'), ('Gigante', 'Gigante')], max_length=15, verbose_name='Porte')),
                ('altura', models.PositiveIntegerField(verbose_name='Altura')),
                ('comprimento', models.PositiveIntegerField(verbose_name='Comprimento')),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=100, unique=True)),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raças', to='ficha.especie')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('peso', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Peso(kg)')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Anotações')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.pet')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
