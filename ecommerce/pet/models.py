from django.db import models

ESPECIE_CHOICES = (
	('cachorro', 'Cachorro'),
	('gato', 'Gato'),
	('coelho', 'Coelho'),
	('cavalo', 'Cavalo'),
	('peixe', 'Peixe')
)

RACA_CACHORRO = (

	('Afegão Hound','Afegão Hound'),
	('Affenpinscher','Affenpinscher'),
	('Airedale Terrier','Airedale Terrier'),
	('Akita', 'Akita'),
	('American Staffordshire Terrier','American Staffordshire Terrier'),
	('Basenji','Basenji'),
	('Basset Hound','Basset Hound'),
	('Beagle','Beagle'),
	('Beagle Harrier','Beagle Harrier'),
	('Bearded Collie','Bearded Collie'),
	('Bedlington Terrier','Bedlington Terrier'),
	('Bichon Frisé','Bichon Frisé'),
	('Bloodhound','Bloodhound'),
	('Bobtail','Bobtail'),
	('Boiadeiro Australiano','Boiadeiro Australiano'),
	('Boiadeiro Bernês','Boiadeiro Bernês'),
	('Border Collie','Border Collie'),
	('Border Terrier','Border Terrier'),
	('Borzoi','Borzoi'),
	('Boston','Boston Terrier'),
	('Boxer','Boxer'),
	('Buldogue Francês','Buldogue Francês'),
	('Buldogue Inglês','Buldogue Inglês'),
	('Bul Terrier','Bull Terrier'),
	('Bulmastife','Bulmastife'),
	('Cairn Terrier','Cairn Terrier'),
	('Cane Corso','Cane Corso'),
	('Cão de Água Português','Cão de Água Português'),
	('Cão de Crista Chinês','Cão de Crista Chinês'),
	('Cavalier King Charles Spaniel','Cavalier King Charles Spaniel'),
	('Chesapeake Bay Retriever','Chesapeake Bay Retriever'),
	('Chihuahua','Chihuahua'),
	('Chow Chow','Chow Chow'),
	('Cocker Spaniel Americano','Cocker Spaniel Americano'),
	('Cocker Spaniel Inglês','Cocker Spaniel Inglês'),
	('Collie','Collie'),
	('Coton de Tuléar','Coton de Tuléar'),
	('Dachshund','Dachshund'),
	('Dálmata','Dálmata'),
	('Dandie Dinmont Terrier','Dandie Dinmont Terrier'),
	('Dobermann','Dobermann'),
	('Dogo Argentino','Dogo Argentino'),
	('Dogue Alemão','Dogue Alemão'),
	('Fila Brasileiro','Fila Brasileiro'),
	('Fox Terrier','Fox Terrier (Pelo Duro e Pelo Liso)'),
	('Foxhound Inglês','Foxhound Inglês'),
	('Galgo Escocês','Galgo Escocês'),
	('Galgo Irlandês','Galgo Irlandês'),
	('Golden Retriever','Golden Retriever'),
	('Grande Boiadeiro Suiço','Grande Boiadeiro Suiço'),
	('Greyhound','Greyhound'),
	('Grifo da Bélgica','Grifo da Bélgica'),
	('Husky Siberiano','Husky Siberiano'),
	('Jack Russell Terrier','Jack Russell Terrier'),
	('King Charles','King Charles'),
	('Komondor','Komondor'),
	('Labradoodle','Labradoodle'),
	('Labrador Retriever','Labrador Retriever'),
	('Lakeland Terrier','Lakeland Terrier'),
	('Leonberger','Leonberger'),
	('Lhasa Apso','Lhasa Apso'),
	('Lulu da Pomerânia','Lulu da Pomerânia'),
	('malamute do Alasca','Malamute do Alasca'),
	('Maltês','Maltês'),
	('Mastife','Mastife'),
	('Mastim Napolitano','Mastim Napolitano'),
	('Mastim Tibetano','Mastim Tibetano'),
	('Norfolk Terrier','Norfolk Terrier'),
	('Norwich Terrier','Norwich Terrier'),
	('Papillon','Papillon'),
	('Pastor Alemão','Pastor Alemão'),
	('Pastor Australiano','Pastor Australiano'),
	('Pastor Suiço', 'Pastor Suiço'),
	('Pinscher Miniatura','Pinscher Miniatura'),
	('Poodle','Poodle'),
	('Pug','Pug'),
	('Rottweiler','Rottweiler'),
	('ShihTzu','ShihTzu'),
	('Silky Terrier','Silky Terrier'),
	('Skye Terrier','Skye Terrier'),
	('Staffordshire Bull Terrier','Staffordshire Bull Terrier'),
	('Terra Nova','Terra Nova'),
	('Terier Escocês','Terrier Escocês'),
	('Tosa','Tosa'),
	('Welsh Corgi (Cardigan)','Welsh Corgi (Cardigan)'),
	('Welsh Corgi (Pembroke)','Welsh Corgi (Pembroke)'),
	('West Highland White Terrier','West Highland White Terrier'),
	('Whippet','Whippet'),
	('Xoloitzcuintli','Xoloitzcuintli'),
	('Yorkshire Terrier','Yorkshire Terrier'),
	('Sem Raça Definida (SRD)','Sem Raça Definida (SRD)'),
	
)

TEMPERAMENTO_CHOICES =(
	('Agressivo','Agressivo'),
    ('Manso','Manso'),
    ('Anti-social','Anti-social'),
    ('Social','Social'),
    ('Agitado','Agitado'),
    ('Calmo','Calmo'),
    ('Introvertido','Introvertido'),
    ('Extrovertido','Extrovertido'),
    ('Obediente','Obediente'),
    ('Independente','Independente'),
    ('Curioso','Curioso'),
    ('Independente','Indiferente'),
    ('Ousado','Ousado'),
    ('Tímido','Tímido'),
)
PELAGEM_CHOICES = (
	('Levemente Aspera','Levemente Aspera'),
	('Fios Lisos e Longos', 'Fios Lisos e Longos')
)
COLORACAO_CHOICES = (
	('amarelo', 'Amarelo'),
	('branco', 'Branco'),
	('caramelo', 'Caramelo'),
	('marrom', 'Marrom'),
	('preto','Preto')
)

class formPet(models.Model):
	nome = models.CharField('Nome',max_length=150)
	apelido = models.CharField('Apelido',max_length=30)
	aniversario = models.DateField('Aniversário', blank=True, null=True)
	idade = models.IntegerField('Idade')
	peso = models.IntegerField('Peso(kg)')
	tamanho = models.IntegerField('Tamanho')
	especie = models.CharField('Especie',max_length=10, choices=ESPECIE_CHOICES)
	racaCachorro = models.CharField('Raça do Cachorro',max_length=150, choices=RACA_CACHORRO)
	temperamento = models.CharField('Temperamento',max_length=60, choices=TEMPERAMENTO_CHOICES)
	pelagem = models.CharField('Pelagem',max_length=150, choices=PELAGEM_CHOICES)
	coloracao = models.CharField('Coloração',max_length=60, choices=COLORACAO_CHOICES)
	tamanho = models.IntegerField('Tamanho(cm)',)
	caracteristicas = models.CharField('Caracteristicas', max_length=200)
	def __str__(self):
		return self.nome	

	


