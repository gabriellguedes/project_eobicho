
class Tuplas():
	
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
	UNHAS_CHOICES = (
		('Normais','Normais'),
		('Grandes', 'Grandes'),
		('Encravadas','Encravadas'),
		('Inflamadas','Inflamadas'),
		('Infeccionadas','Infeccionadas'),
	)
	ECTOPARASITAS_CHOICES = (
		('Pulgas','Pulgas'),
		('Piolho','Piolho'),
		('Carrapato','Carrapato'),
		('Verme','Verme'),
		('Miase','Miase'),
	)
	PELE_INFECCIONADA_CHOICES = (
		('Dermatite','Dermatite'),
		('Micose','Micose'),
	)
	PELE_OUTROS_CHOICES =(
		('Oleosa','Oleosa'),
		('Plurido','Plurido'),
		('Seborea','Seborea'),
	)
	PELOS_CHOICES = (
		('Ressecado','Ressecado'),
		('Danificado','Danificado'),

	)
	PELOS_ESTADO_CHOICES = (
		('Limpo','Limpo'),
		('Pouco Sujo','Pouco Sujo'),
		('Sujo','Sujo'),
		('Muito Sujo','Muito Sujo'),
		('Encardido','Encardido'),
	)
	PELOS_CONDICAO_CHOICES = (
		('Livre','Livre'),
		('Bagunçado','Bagunçado'),
		('Embaraçado','Embaraçado'),
		('Embaraçado com bola reversível','Embaraçado com bola reversível'),
		('Embaraçado com bola irreversível','Embaraçado com bola irreversível'),
		('Crítico','Crítico'),
	)
	BOCA_CHOICES = (
		('Gengivite','Gengivite'),
		('Doença Periodontal','Doença Periodontal'),
		('Lesões endodônticas','Lesões endodônticas'),
	)
	OLHOS_CHOICES = (
		('Inflamados','Inflamados'),
		('QueimadoGlaucoma','Glaucoma'),
		('Catarata','Catarata'),
		('Queimado','Queimado'),
		('Alergia','Alergia'),
		('Úlcera na Córnea','Úlcera na Córnea'),
		('Uveíte','Uveíte'),
		('Conjuntivite(Ceratoconjuntivite Seca)','Conjuntivite(Ceratoconjuntivite Seca)'),
	)
	PATAS_CHOICES = (
		('Calo','Calo'),
		('Lesionados','Lesionados'),
		('Infeccionado','Infeccionado'),
		('Inflamados','Inflamados'),
		('Bicho de pé','Bicho de pé'),
	)
	ORELHAS_CHOICES =(
		('Infecção','Infecção'),
		('Inflamação','Inflamação'),
	)

