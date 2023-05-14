from database import Database
from jogadores_database import JogoDaresDatabase
import json

# Conectando com o banco de dados
db = Database("bolt://54.156.105.132:7687", "neo4j", "fasteners-departure-grounds")
db.drop_all()

# Criando um objeto da classe JogoDaresDatabase
jogadores_db = JogoDaresDatabase(db)

# Criando alguns jogadores
jogadores_db.create_player('John', 1)
jogadores_db.create_player('Alice', 2)
jogadores_db.create_player('Bob', 3)

# Atualizando um jogador
jogadores_db.update_player(1, name='Johnny')

# Deletando um jogador
jogadores_db.delete_player(3)

# Criando uma partida com dois jogadores
result_dict = {"Johnny": 10, "Alice": 8}
result_json = json.dumps(result_dict)

jogadores_db.create_match(1, result=result_json)

# Adicionando jogadores à partida
jogadores_db.add_player_to_match(1, jogadores_db.get_player(1))
jogadores_db.add_player_to_match(1, jogadores_db.get_player(2))


# Obtendo informações de uma partida
match = jogadores_db.get_match(1)
print(f"Match ID: {match['match_id']}\n"
      f"Match Result: {match['match_result']}\n"
      f"Players: {[p['name'] for p in match['players']]}")

# Obtendo histórico de partidas de um jogador
matches = jogadores_db.get_player_matches(1)
print(f"Matches for player ID 1: {[m['match_result'] for m in matches]}")

# Fechando a conexão com o banco de dados
db.close()
