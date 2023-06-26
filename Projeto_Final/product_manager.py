from product import Product
from store import Store

class ProductManager:
    def __init__(self, database):
        self.db = database

    def cadastrar_produto(self):
        name = input("Digite o nome do produto: ")
        category = input("Digite a categoria do produto (Periféricos, Hardware, Software): ")
        price = float(input("Digite o preço do produto: "))
        discount = float(input("Digite o desconto do produto (em porcentagem): "))
        quantity = int(input("Digite a quantidade do produto: "))

        product = Product(name, category, price, discount, quantity)
        self.salvar_produto(product)

        print("Produto cadastrado com sucesso!")

    def salvar_produto(self, product):
        query = """
            CREATE (p:Product {name: $name, category: $category, price: $price, discount: $discount, quantity: $quantity})
        """
        parameters = product.to_dict()
        self.db.execute_query(query, parameters)

    def buscar_produto(self, product_name):
        query = """
            MATCH (p:Product {name: $product_name})
            RETURN p
        """
        parameters = {'product_name': product_name}
        result = self.db.execute_query(query, parameters)
        if result:
            return Product(**result[0]['p'])
        else:
            return None

    def listar_produtos(self):
        product_name = input("Digite o nome do produto: ")
        query = """
            MATCH (p:Product {name: $product_name})
            OPTIONAL MATCH (p)-[:VENDIDO_EM]->(s:Store)
            RETURN p.name AS product_name, p.category AS category, p.price AS price, p.discount AS discount, 
                   p.quantity AS quantity, s.name AS store_name
        """
        parameters = {'product_name': product_name}
        result = self.db.execute_query(query, parameters)

        if result:
            for record in result:
                product_name = record['product_name']
                category = record['category']
                price = record['price']
                discount = record['discount']
                quantity = record['quantity']
                store_name = record['store_name']

                product = Product(product_name, category, price, discount, quantity)

                print("Nome: ", product.name)
                print("Categoria: ", product.category)
                print("Preço: R$ ", product.price)
                print("Preço com desconto: R$ ", product.calcular_preco_com_disconto())
                print("Quantidade: ", product.quantity)

                if store_name:
                    print("Loja: ", store_name)

                print("-----")
        else:
            print("Nenhum produto encontrado.")

    def deletar_produto(self):
        product_name = input("Digite o nome do produto que deseja deletar: ")
        product = self.buscar_produto(product_name)

        if product:
            self.remover_relacionamentos_produto(product)
            self.remover_produto(product)
            print(f"Produto '{product.name}' deletado com sucesso!")
        else:
            print("Produto não encontrado.")

    def atualizar_produto(self):
        product_name = input("Digite o nome do produto que deseja atualizar: ")
        product = self.buscar_produto(product_name)

        if product:
            new_name = input("Digite o novo nome do produto: ")
            new_category = input("Digite a nova categoria do produto (Periféricos, Hardware, Software): ")
            new_price = float(input("Digite o novo preço do produto: "))
            new_discount = float(input("Digite o novo desconto do produto (em porcentagem): "))
            new_quantity = int(input("Digite a nova quantidade do produto: "))

            product.name = new_name
            product.category = new_category
            product.price = new_price
            product.discount = new_discount
            product.quantity = new_quantity

            self.atualizar_produto_no_banco(product)
            print(f"Produto '{product_name}' atualizado com sucesso!")
        else:
            print("Produto não encontrado.")

    def vender_produto_na_loja(self, product, store):
        query = """
            MATCH (p:Product {name: $product_name}), (s:Store {name: $store_name})
            CREATE (p)-[:VENDIDO_EM]->(s)
        """
        parameters = {'product_name': product.name, 'store_name': store.name}
        self.db.execute_query(query, parameters)

    def incluir_hardware_no_computador(self, hardware, computer):
        query = """
            MATCH (h:Product {name: $hardware_name}), (c:Product {name: $computer_name})
            CREATE (h)-[:INCLUI]->(c)
        """
        parameters = {'hardware_name': hardware.name, 'computer_name': computer.name}
        self.db.execute_query(query, parameters)

    def remover_relacionamentos_produto(self, product):
        query = """
            MATCH (p:Product {name: $product_name})-[r]-()
            DELETE r
        """
        parameters = {'product_name': product.name}
        self.db.execute_query(query, parameters)

    def remover_produto(self, product):
        query = """
            MATCH (p:Product {name: $product_name})
            DELETE p
        """
        parameters = {'product_name': product.name}
        self.db.execute_query(query, parameters)

    def atualizar_produto_no_banco(self, product):
        query = """
            MATCH (p:Product {name: $product_name})
            SET p.name = $new_name,
                p.category = $new_category,
                p.price = $new_price,
                p.discount = $new_discount,
                p.quantity = $new_quantity
        """
        parameters = {
            'product_name': product.name,
            'new_name': product.name,
            'new_category': product.category,
            'new_price': product.price,
            'new_discount': product.discount,
            'new_quantity': product.quantity
        }
        self.db.execute_query(query, parameters)


