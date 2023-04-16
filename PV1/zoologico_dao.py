from bson.objectid import ObjectId

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
