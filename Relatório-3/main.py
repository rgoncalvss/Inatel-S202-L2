from save_json import writeAJson
from database import Database


db = Database(database="dex", collection="pokemons")
db.resetDatabase()
pokemons = db.collection.find()
for pokemon in pokemons: #printando ela
    print(pokemon)

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})

bulbasaur = getPokemonByDex(1)
writeAJson(bulbasaur, "bulbasaur")

def getPokemonByName(name: str):
    return db.collection.find({"name.english": name})

charizard = getPokemonByName("Charizard")
writeAJson(charizard, "charizard")

pokemon = db.collection.find({"type": "Grass", "base.Attack": { "$lte": 50 }})
writeAJson(pokemon, "pokemon_grass")

pokemon_ghost = db.collection.find({"type": "Ghost"})
writeAJson(pokemon_ghost, "pokemon_ghost")

def get_4_letters_or_less(collection):
  names = collection.find({}, {"name": 1})
  four_letters_or_less = []
  for name in names:
    if len(name["name"].keys()) <= 4:
      if all(len(word) <= 4 for word in name["name"].values()):
        four_letters_or_less.append(name["name"].values())
  return four_letters_or_less

writeAJson(get_4_letters_or_less(db.collection), "pokemon_4_words_or_less")