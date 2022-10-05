import django
from ecommerce.pet.models import Pet, Especie, Raca
from ecommerce.pet.tuplas import Tuplas
from ecommerce.ficha.models import Ficha

def run():
    tupla = Tuplas()
    cachorro = tupla.RACA_CACHORRO
    lista = []

    for item in cachorro:
        for x in item:
            if x in lista:
                pass
            else:
                lista.append(x)

    return print(lista)
