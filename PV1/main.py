import json

import pymongo
from bson.objectid import ObjectId


class Database:
    def __init__(self, uri, database):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[database]

    def close(self):
        self.client.close()


class ZoologicoDAO:
    def __init__(self, database):
        self.db = database
        self.animais = self.db.db.Animais

    def create_animal(self, animal):
        result = self.animais.insert_one(animal)
        return result.inserted_id

    def read_animal(self, id):
        animal = self.animais.find_one({'_id': ObjectId(id)})
        animal['_id'] = str(animal['_id'])
        return animal

    def update_animal(self, id, new_animal):
        result = self.animais.replace_one({'_id': ObjectId(id)}, new_animal)
        return result.modified_count

    def delete_animal(self, id):
        result = self.animais.delete_one({'_id': ObjectId(id)})
        return result.deleted_count


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


db = Database("mongodb://localhost:27017/", "zoo")

zoo_cli = ZoologicoCLI(db)
zoo_dao = ZoologicoDAO(db)


#zoo_cli.create_animal()
animal = zoo_dao.read_animal('643c77bad9997b6e380beaa6')
print(json.dumps(animal, indent=4, default=str, ensure_ascii=False))


