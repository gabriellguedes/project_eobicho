
def Cadastro(tupla):
	bd = input('Digite o caminho até o models: ')
	
	if bd == 'Boca': 
		from ecommerce.ficha.boca.models import Boca
		objeto = Boca.objects.all()
	elif bd == 'Patas':
		from ecommerce.ficha.patas.models import Patas
		objeto = Patas.objects.all()
	elif bd == 'Pele':
		from ecommerce.ficha.pele.models import Pele
		objeto = Pele.objects.all()
	elif bd == 'Pele_Doenca':
		from ecommerce.ficha.pele.models import DoencaPele
		objeto = DoencaPele.objects.all()
	elif bd == 'Pelos':
		from ecommerce.ficha.pelos.models import Pelos
		objeto = Pelos.objects.all()
	elif bd == 'Pelos_Estado':
		from ecommerce.ficha.pelos.models import Estado_pelos
		objeto = Estado_pelos.objects.all()
	elif bd == 'Pelos_Condicao':
		from ecommerce.ficha.pelos.models import Condicao_pelos
		objeto = Condicao_pelos.objects.all()
	elif bd == 'Unhas':
		from ecommerce.ficha.unhas.models import Unhas
		objeto = Unhas.objects.all()
	elif bd == 'Orelhas':
		from ecommerce.ficha.orelhas.models import Orelhas
		objeto = Orelhas.objects.all()
	elif bd == 'Olhos':
		from ecommerce.ficha.olhos.models import Olhos
		objeto = Olhos.objects.all()
	elif bd == 'Ectoparasitas':
		from ecommerce.ficha.pele.models import Ectoparasitas
		objeto = Ectoparasitas.objects.all()
	elif bd == 'Coloracao':
		from ecommerce.ficha.pelos.models import Coloracao
		objeto = Coloracao.objects.all()
	elif bd == 'Pelagem':
		from ecommerce.ficha.pelos.models import Pelagem
		objeto = Pelagem.objects.all()
	else:
		print("opção invalida, tente novamente.")
	
	lista = []
	
	for x in tupla:
		for y in x:
			if y in lista:
				pass
			else:
				lista.append(y)
				objeto.create(nome=y)
				print(y, 'foi cadastrado no banco de dados!')
				print("################################################################")
				



class Tuplas():
	PORTE_RACAS_CHOICES = (
		('Pequeno', 'Pequeno'),
		('Medio', 'Médio'),
		('Grande', 'Grande'),
		('Gigante', 'Gigante'),
	)

	CARGOS_CHOICES = [
			('Gerente', 'Gerente'),
			('Medico Veterinario', 'Médico Veterinário'),
			('Colaborador', 'Colaborador'),
			('Cliente', 'Cliente'),
		]
	UF_CHOICES = (
		('AC','AC'),
		('AL', 'AL'), 
		('AP', 'AP'), 
		('AM', 'AM'), 
		('BA', 'BA'), 
		('CE', 'CE'), 
		('DF', 'DF'), 
		('ES', 'ES'),
		('GO','GO'),
		('MA','MA'),
		('MT','MT'),
		('MS','MS'),
		('MG','MG'),
		('PA','PA'),
		('PB','PB'),
		('PR','PR'),
		('PE','PE'),
		('PI','PI'),
		('RJ','RJ'),
		('RN','RN'),
		('RS','RS'),
		('RO','RO'),
		('RR','RR'),
		('SC','SC'),
	)
	SEXO_CHOICES = (
		('Macho','Macho'),
		('Fêmia', 'Fêmia'),
	)
	
	ESPECIE_CHOICES = (
		('Cachorro', 'Cachorro'),
		('Gato', 'Gato'),
		('Coelho', 'Coelho'),
		('Cavalo', 'Cavalo'),
		('Peixe', 'Peixe')
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
		('Malamute do Alasca','Malamute do Alasca'),
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

	RACA_GATO = (
		('Abissínio', 'Abissínio'),
		('Angorá', 'Angorá'),
		('Balinês', 'Balinês'),
		('Bengal', 'Bengal'),
		('Bobtail americano', 'Bobtail americano'),
		('Bobtail japonês', 'Bobtail japonês'),
		('Bombay', 'Bombay'),
		('Burmês', 'Burmês'),
		('Burmês vermelho', 'Burmês vermelho'),
		('Chartreux', 'Chartreux'),
		('Colorpoint de Pêlo Curto', 'Colorpoint de Pêlo Curto'),
		('Cornish Rex', 'Cornish Rex'),
		('Curl Americano', 'Curl Americano'),
		('Devon Rex', 'Devon Rex'),
		('Himalaio', 'Himalaio'),
		('Jaguatirica', 'Jaguatirica'),
		('Javanês', 'Javanês'),
		('Korat', 'Korat'),
		('LaPerm', 'LaPerm'),
		('Maine Coon', 'Maine Coon'),
		('Manx', 'Manx'),
		('Cymric', 'Cymric'),
		('Mau Egípcio', 'Mau Egípcio'),
		('Mist Australiano', 'Mist Australiano'),
		('Munchkin', 'Munchkin'),
		('Norueguês da Floresta', 'Norueguês da Floresta'),
		('Pelo curto americano', 'Pelo curto americano'),
		('Pelo curto brasileiro', 'Pelo curto brasileiro'),
		('Pelo curto europeu', 'Pelo curto europeu'),
		('Pelo curto inglês', 'Pelo curto inglês'),
		('Persa', 'Persa'),
		('Pixie-bob', 'Pixie-bob'),
		('Ragdoll', 'Ragdoll'),
		('Ocicat', 'Ocicat'),
		('Russo Azul', 'Russo Azul'),
		('Sagrado da Birmânia', 'Sagrado da Birmânia'),
		('Savannah', 'Savannah'),
		('Scottish Fold', 'Scottish Fold'),
		('Selkirk Rex', 'Selkirk Rex'),
		('Siamês', 'Siamês'),
		('Siberiano', 'Siberiano'),
		('Singapura', 'Singapura'),
		('Somali', 'Somali'),
		('Sphynx', 'Sphynx'),
		('Thai', 'Thai'),
		('Tonquinês', 'Tonquinês'),
		('Toyger', 'Toyger'),
		('Usuri', 'Usuri'),
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
		('Armada','Armada'),
		('Aspera', 'Aspera'),
		('Dura', 'Dura'),
		('Encaracolada','Encaracolada'),
		('Levemente Aspera','Levemente Aspera'),
		('Lisa', 'Lisa'),
		('Ondulada', 'Ondulada'),
		('Sedosa', 'Sedosa'),
	)
	TYPE_PELO_CHOICES =(
		('Curto', 'Curto'),
		('Medio', 'Medio'),
		('Longo', 'Longo'),
		('Muito Longo', 'Muito Longo'),
	)

	COLORACAO_CHOICES = (
		('Albino', 'Albino'),
		('amarelo', 'Amarelo'),
		('branco', 'Branco'),
		('caramelo', 'Caramelo'),
		('Chocolate', 'Chocolate'),
		('Cinza', 'Cinza'),
		('Dourado', 'Dourado'),
		('Vermelho','Vermelho'),
		('preto','Preto'),

	)
	UNHAS_CHOICES = (
		('Normais','Normais'),
		('Grandes', 'Grandes'),
		('Encravadas','Encravadas'),
		('Inflamadas','Inflamadas'),
		('Infeccionadas','Infeccionadas'),
	)
	ECTOPARASITAS_CHOICES = (
		('Sem Ectoparasitas','Sem Ectoparasitas'),
		('Pulgas','Pulgas'),
		('Piolho','Piolho'),
		('Carrapato','Carrapato'),
		('Verme','Verme'),
		('Miase','Miase'),
	)
	PELE_INFECCIONADA_CHOICES = (
		('Normal','Normal'),
		('Dermatite','Dermatite'),
		('Micose','Micose'),
	)
	PELE_OUTROS_CHOICES =(
		('Normal', 'Normal'),
		('Oleosa','Oleosa'),
		('Plurido','Plurido'),
		('Seborea','Seborea'),
	)
	PELOS_CHOICES = (
		('Hidratados', 'Hidratatos'),
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
		('Normal','Normal'),
		('Gengivite','Gengivite'),
		('Doença Periodontal','Doença Periodontal'),
		('Lesões endodônticas','Lesões endodônticas'),
	)
	OLHOS_CHOICES = (
		('Normais', 'Normais'),
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
		('Normais','Normais'),
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
	DOENCA_CHOICES = (
		('Sem Doenças', 'Sem Doença'),
		('Leishmaniose','Leishmaniose'),
		('Doença Gastro Intestinal','Doença Gastro Intestinal'),
		('Trauma Cutaneo','Trauma Cutaneo'),
		('Hemorragia','Hemorragia'),
	)

