from database import Database


class JogoDaresDatabase(Database):
    def __init__(self, database):
        self.db = database

    def create_player(self, name, player_id):
        query = "CREATE (p:Player {name: $name, player_id: $player_id})"
        parameters = {'name': name, 'player_id': player_id}
        self.db.execute_query(query, parameters)

    def update_player(self, player_id, **kwargs):
        set_clause = ", ".join([f"p.{key} = ${key}" for key in kwargs])
        query = f"MATCH (p:Player {{player_id: $player_id}}) SET {set_clause}"
        parameters = {'player_id': player_id, **kwargs}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_id):
        query = "MATCH (p:Player {player_id: $player_id}) DETACH DELETE p"
        parameters = {'player_id': player_id}
        self.db.execute_query(query, parameters)

    def get_player(self, player_id):
        query = "MATCH (p:Player {player_id: $player_id}) RETURN p"
        parameters = {'player_id': player_id}
        result = self.db.execute_query(query, parameters)
        if result:
            return result[0]['p']
        else:
            return None

    def create_match(self, match_id, result):
        query = "CREATE (m:Match {match_id: $match_id, result: $result})"
        parameters = {'match_id': match_id, 'result': result}
        self.db.execute_query(query, parameters)

    def add_player_to_match(self, match_id, player):
        query = "MATCH (p:Player {player_id: $player_id}), (m:Match {match_id: $match_id}) CREATE (p)-[:PARTICIPATED_IN]->(m)"
        parameters = {'player_id': player['player_id'], 'match_id': match_id}
        self.db.execute_query(query, parameters)

    def get_match(self, match_id):
        query = """
            MATCH (m:Match {match_id: $match_id})<-[:PARTICIPATED_IN]-(p:Player)
            RETURN m.match_id AS match_id, m.result AS match_result, collect({name: p.name, player_id: p.player_id}) AS players
        """
        parameters = {'match_id': match_id}
        result = self.db.execute_query(query, parameters)
        if result:
            return result[0]
        else:
            return None

    def get_player_matches(self, player_id):
        query = """
            MATCH (p:Player {player_id: $player_id})-[:PARTICIPATED_IN]->(m:Match)
            RETURN m.match_id AS match_id, m.result AS match_result, collect({name: p.name, player_id: p.player_id}) AS players
        """
        parameters = {'player_id': player_id}
        result = self.db.execute_query(query, parameters)
        return result
