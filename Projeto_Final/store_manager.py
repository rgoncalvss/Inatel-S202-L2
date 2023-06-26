from store import Store

class StoreManager:
    def __init__(self, database):
        self.db = database

    def cadastrar_loja(self):
        name = input("Digite o nome da loja: ")

        store = Store(name)
        self.salvar_loja(store)

        print("Loja cadastrada com sucesso!")

    def salvar_loja(self, store):
        query = """
            CREATE (s:Store {name: $name})
        """
        parameters = store.to_dict()
        self.db.execute_query(query, parameters)

    def buscar_lojas(self, store_name=None):
        query = """
            MATCH (s:Store)
            """
        if store_name:
            query += "WHERE s.name = $store_name "

        query += "RETURN s"

        parameters = {'store_name': store_name} if store_name else {}
        result = self.db.execute_query(query, parameters)

        if result:
            stores = []
            for record in result:
                store = Store(**record['s'])
                stores.append(store)
            return stores
        else:
            return None

    def listar_lojas(self):
        stores = self.buscar_lojas()

        if stores:
            for store in stores:
                print("Nome da Loja: ", store.name)
                print("-----")
        else:
            print("Nenhuma loja encontrada.")
