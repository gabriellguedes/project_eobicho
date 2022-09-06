# Generated by Django 4.1 on 2022-09-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_anamnesemodel_petmodel_delete_formpet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anamnesemodel',
            name='obs',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='boca',
            field=models.CharField(blank=True, choices=[('Gengivite', 'Gengivite'), ('Doença Periodontal', 'Doença Periodontal'), ('Lesões endodônticas', 'Lesões endodônticas')], max_length=100, null=True, verbose_name='Boca'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='ectoparasitas',
            field=models.CharField(blank=True, choices=[('Pulgas', 'Pulgas'), ('Piolho', 'Piolho'), ('Carrapato', 'Carrapato'), ('Verme', 'Verme'), ('Miase', 'Miase')], max_length=100, null=True, verbose_name='Ectoparasitas'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='olhos',
            field=models.CharField(blank=True, choices=[('Inflamados', 'Inflamados'), ('QueimadoGlaucoma', 'Glaucoma'), ('Catarata', 'Catarata'), ('Queimado', 'Queimado'), ('Alergia', 'Alergia'), ('Úlcera na Córnea', 'Úlcera na Córnea'), ('Uveíte', 'Uveíte'), ('Conjuntivite(Ceratoconjuntivite Seca)', 'Conjuntivite(Ceratoconjuntivite Seca)')], max_length=100, null=True, verbose_name='Olhos'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='orelhas',
            field=models.CharField(blank=True, choices=[('Infecção', 'Infecção'), ('Inflamação', 'Inflamação')], max_length=100, null=True, verbose_name='Orelhas'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='patas',
            field=models.CharField(blank=True, choices=[('Calo', 'Calo'), ('Lesionados', 'Lesionados'), ('Infeccionado', 'Infeccionado'), ('Inflamados', 'Inflamados'), ('Bicho de pé', 'Bicho de pé')], max_length=100, null=True, verbose_name='Patas'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='peleInfeccionada',
            field=models.CharField(blank=True, choices=[('Dermatite', 'Dermatite'), ('Micose', 'Micose')], max_length=100, null=True, verbose_name='Infecção na Pele'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='peleOutros',
            field=models.CharField(blank=True, choices=[('Oleosa', 'Oleosa'), ('Plurido', 'Plurido'), ('Seborea', 'Seborea')], max_length=100, null=True, verbose_name='Outros'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='pelos',
            field=models.CharField(blank=True, choices=[('Ressecado', 'Ressecado'), ('Danificado', 'Danificado')], max_length=100, null=True, verbose_name='Pelos'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='pelosCondicao',
            field=models.CharField(blank=True, choices=[('Livre', 'Livre'), ('Bagunçado', 'Bagunçado'), ('Embaraçado', 'Embaraçado'), ('Embaraçado com bola reversível', 'Embaraçado com bola reversível'), ('Embaraçado com bola irreversível', 'Embaraçado com bola irreversível'), ('Crítico', 'Crítico')], max_length=100, null=True, verbose_name='Condição dos Pelos'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='pelosEstado',
            field=models.CharField(blank=True, choices=[('Limpo', 'Limpo'), ('Pouco Sujo', 'Pouco Sujo'), ('Sujo', 'Sujo'), ('Muito Sujo', 'Muito Sujo'), ('Encardido', 'Encardido')], max_length=100, null=True, verbose_name='Estado do Pelo'),
        ),
        migrations.AlterField(
            model_name='anamnesemodel',
            name='unhas',
            field=models.CharField(blank=True, choices=[('Normais', 'Normais'), ('Grandes', 'Grandes'), ('Encravadas', 'Encravadas'), ('Inflamadas', 'Inflamadas'), ('Infeccionadas', 'Infeccionadas')], max_length=100, null=True, verbose_name='Unhas'),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='coloracao',
            field=models.CharField(blank=True, choices=[('Albino', 'Albino'), ('amarelo', 'Amarelo'), ('branco', 'Branco'), ('caramelo', 'Caramelo'), ('Chocolate', 'Chocolate'), ('Cinza', 'Cinza'), ('Dourado', 'Dourado'), ('Vermelho', 'Vermelho'), ('preto', 'Preto')], max_length=60, null=True, verbose_name='Coloração'),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='idade',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True, verbose_name='Peso(kg)'),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='racaCachorro',
            field=models.CharField(blank=True, choices=[('Afegão Hound', 'Afegão Hound'), ('Affenpinscher', 'Affenpinscher'), ('Airedale Terrier', 'Airedale Terrier'), ('Akita', 'Akita'), ('American Staffordshire Terrier', 'American Staffordshire Terrier'), ('Basenji', 'Basenji'), ('Basset Hound', 'Basset Hound'), ('Beagle', 'Beagle'), ('Beagle Harrier', 'Beagle Harrier'), ('Bearded Collie', 'Bearded Collie'), ('Bedlington Terrier', 'Bedlington Terrier'), ('Bichon Frisé', 'Bichon Frisé'), ('Bloodhound', 'Bloodhound'), ('Bobtail', 'Bobtail'), ('Boiadeiro Australiano', 'Boiadeiro Australiano'), ('Boiadeiro Bernês', 'Boiadeiro Bernês'), ('Border Collie', 'Border Collie'), ('Border Terrier', 'Border Terrier'), ('Borzoi', 'Borzoi'), ('Boston', 'Boston Terrier'), ('Boxer', 'Boxer'), ('Buldogue Francês', 'Buldogue Francês'), ('Buldogue Inglês', 'Buldogue Inglês'), ('Bul Terrier', 'Bull Terrier'), ('Bulmastife', 'Bulmastife'), ('Cairn Terrier', 'Cairn Terrier'), ('Cane Corso', 'Cane Corso'), ('Cão de Água Português', 'Cão de Água Português'), ('Cão de Crista Chinês', 'Cão de Crista Chinês'), ('Cavalier King Charles Spaniel', 'Cavalier King Charles Spaniel'), ('Chesapeake Bay Retriever', 'Chesapeake Bay Retriever'), ('Chihuahua', 'Chihuahua'), ('Chow Chow', 'Chow Chow'), ('Cocker Spaniel Americano', 'Cocker Spaniel Americano'), ('Cocker Spaniel Inglês', 'Cocker Spaniel Inglês'), ('Collie', 'Collie'), ('Coton de Tuléar', 'Coton de Tuléar'), ('Dachshund', 'Dachshund'), ('Dálmata', 'Dálmata'), ('Dandie Dinmont Terrier', 'Dandie Dinmont Terrier'), ('Dobermann', 'Dobermann'), ('Dogo Argentino', 'Dogo Argentino'), ('Dogue Alemão', 'Dogue Alemão'), ('Fila Brasileiro', 'Fila Brasileiro'), ('Fox Terrier', 'Fox Terrier (Pelo Duro e Pelo Liso)'), ('Foxhound Inglês', 'Foxhound Inglês'), ('Galgo Escocês', 'Galgo Escocês'), ('Galgo Irlandês', 'Galgo Irlandês'), ('Golden Retriever', 'Golden Retriever'), ('Grande Boiadeiro Suiço', 'Grande Boiadeiro Suiço'), ('Greyhound', 'Greyhound'), ('Grifo da Bélgica', 'Grifo da Bélgica'), ('Husky Siberiano', 'Husky Siberiano'), ('Jack Russell Terrier', 'Jack Russell Terrier'), ('King Charles', 'King Charles'), ('Komondor', 'Komondor'), ('Labradoodle', 'Labradoodle'), ('Labrador Retriever', 'Labrador Retriever'), ('Lakeland Terrier', 'Lakeland Terrier'), ('Leonberger', 'Leonberger'), ('Lhasa Apso', 'Lhasa Apso'), ('Lulu da Pomerânia', 'Lulu da Pomerânia'), ('malamute do Alasca', 'Malamute do Alasca'), ('Maltês', 'Maltês'), ('Mastife', 'Mastife'), ('Mastim Napolitano', 'Mastim Napolitano'), ('Mastim Tibetano', 'Mastim Tibetano'), ('Norfolk Terrier', 'Norfolk Terrier'), ('Norwich Terrier', 'Norwich Terrier'), ('Papillon', 'Papillon'), ('Pastor Alemão', 'Pastor Alemão'), ('Pastor Australiano', 'Pastor Australiano'), ('Pastor Suiço', 'Pastor Suiço'), ('Pinscher Miniatura', 'Pinscher Miniatura'), ('Poodle', 'Poodle'), ('Pug', 'Pug'), ('Rottweiler', 'Rottweiler'), ('ShihTzu', 'ShihTzu'), ('Silky Terrier', 'Silky Terrier'), ('Skye Terrier', 'Skye Terrier'), ('Staffordshire Bull Terrier', 'Staffordshire Bull Terrier'), ('Terra Nova', 'Terra Nova'), ('Terier Escocês', 'Terrier Escocês'), ('Tosa', 'Tosa'), ('Welsh Corgi (Cardigan)', 'Welsh Corgi (Cardigan)'), ('Welsh Corgi (Pembroke)', 'Welsh Corgi (Pembroke)'), ('West Highland White Terrier', 'West Highland White Terrier'), ('Whippet', 'Whippet'), ('Xoloitzcuintli', 'Xoloitzcuintli'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Sem Raça Definida (SRD)', 'Sem Raça Definida (SRD)')], max_length=150, null=True, verbose_name='Raça do Cachorro'),
        ),
    ]
