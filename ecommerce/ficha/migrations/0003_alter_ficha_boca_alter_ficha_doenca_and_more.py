# Generated by Django 4.1 on 2022-10-06 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0002_boca_condicao_pelos_doenca_ectoparasitas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='boca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.boca', verbose_name='Boca'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='doenca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.doenca', verbose_name='Doença'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='ectoparasitas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.ectoparasitas', verbose_name='Ectoparasitas'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='olhos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.olhos', verbose_name='Olhos'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='orelhas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.orelhas', verbose_name='Orelhas'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='patas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.patas', verbose_name='Patas'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='pele',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.pele', verbose_name='Tipo de Pele'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='peleInfeccionada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.infec_pele', verbose_name='Doença na Pele'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='pelos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.pelos', verbose_name='Pelos'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='pelosCondicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.condicao_pelos', verbose_name='Condição dos Pelos'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='pelosEstado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.estado_pelos', verbose_name='Estado dos Pelos'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='unhas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.unhas', verbose_name='Unhas'),
        ),
    ]