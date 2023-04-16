import json

from zoologico_dao import ZoologicoDAO
from database import Database

class ZoologicoCLI:
    def __init__(self, database):
        self.dao = ZoologicoDAO(database)

    def create_animal(self):
        cuidador = {
            'nome': input('Nome do cuidador: '),
            'documento': input('Documento do cuidador: ')
        }

        habitats = []
        while True:
            habitat_nome = input('Nome do habitat: ')
            habitat_tipo = input('Tipo do ambiente: ')
            habitat_cuidador = cuidador.copy()
            habitats.append({
                'nome': habitat_nome,
                'tipoAmbiente': habitat_tipo,
                'cuidador': habitat_cuidador
            })

            if input('Deseja adicionar outro habitat? (S/N): ').lower() == 'n':
                break

        animal = {
            'nome': input('Nome do animal: '),
            'especie': input('Espécie do animal: '),
            'idade': int(input('Idade do animal: ')),
            'habitat': habitats
        }

        result = self.dao.create_animal(animal)
        print(f"Animal criado com ID {result}")

