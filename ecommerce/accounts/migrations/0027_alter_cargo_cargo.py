# Generated by Django 4.1.3 on 2022-11-22 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_alter_cargo_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(blank=True, choices=[('Gerente', 'Gerente'), ('Medico Veterinario', 'Médico Veterinário'), ('Colaborador', 'Colaborador'), ('Cliente', 'Cliente')], max_length=50, null=True, verbose_name='Cargo'),
        ),
    ]