from database import Database
from zoologico_cli import ZoologicoCLI
from zoologico_dao import ZoologicoDAO
import json

db = Database("mongodb://localhost:27017/", "zoo")
zoo_cli = ZoologicoCLI(db)
zoo_dao = ZoologicoDAO(db)

#zoo_cli.create_animal()
animal = zoo_dao.read_animal('643c77bad9997b6e380beaa6')
print(json.dumps(animal, indent=4, default=str, ensure_ascii=False))
