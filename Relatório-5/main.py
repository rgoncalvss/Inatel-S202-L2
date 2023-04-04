import jsonschema
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['biblioteca']
livros_collection = db['livros']

livro_schema = {
    "type": "object",
    "properties": {
        "_id": {"type": "integer"},
        "titulo": {"type": "string"},
        "autor": {"type": "string"},
        "ano": {"type": "integer"},
        "preco": {"type": "number"}
    },
    "required": ["_id", "titulo", "autor", "ano", "preco"]
}

livro1 = {
    "_id": 1,
    "titulo": "Moby Dick",
    "autor": "Herman Melville",
    "ano": 1851,
    "preco": 25.0
}

livro2 = {
    "_id": 2,
    "titulo": "1984",
    "autor": "George Orwell",
    "ano": 1949,
    "preco": 20.0,
}

livros_collection.insert_one(livro1)
livros_collection.insert_one(livro2)

livro = livros_collection.find_one({"_id": 1})
print(livro)

livros_collection.update_one({"_id": 2}, {"$set": {"preco": 18.0}})
livro = livros_collection.find_one({"_id": 2})
print(livro)

livros_collection.delete_one({"_id": 1})
livro = livros_collection.find_one({"_id": 1})
print(livro)

for livro in livros_collection.find():
    jsonschema.validate(livro, livro_schema)
