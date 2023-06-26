from product_manager import ProductManager
from store_manager import StoreManager


class Menu:
    def __init__(self, database):
        self.db = database
        self.product_manager = ProductManager(database)
        self.store_manager = StoreManager(database)

    def exibir_menu(self):
        while True:
            print("1. Cadastrar Produto")
            print("2. Listar Produtos")
            print("3. Deletar Produto")
            print("4. Atualizar Produto")
            print("5. Cadastrar Loja")
            print("6. Listar Lojas")
            print("7. Adicionar Produto à Loja")
            print("0. Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.product_manager.cadastrar_produto()
            elif opcao == "2":
                self.product_manager.listar_produtos()
            elif opcao == "3":
                self.product_manager.deletar_produto()
            elif opcao == "4":
                self.product_manager.atualizar_produto()
            elif opcao == "5":
                self.store_manager.cadastrar_loja()
            elif opcao == "6":
                self.store_manager.listar_lojas()
            elif opcao == "7":
                self.adicionar_produto_a_loja()
            elif opcao == "8":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def adicionar_produto_a_loja(self):
        product_name = input("Digite o nome do produto: ")
        store_name = input("Digite o nome da loja: ")

        product = self.product_manager.buscar_produto(product_name)
        stores = self.store_manager.buscar_lojas(store_name)

        if product and stores:
            selected_store = stores[0]  # Seleciona a primeira loja da lista
            self.product_manager.vender_produto_na_loja(product, selected_store)
            print("Produto adicionado à loja com sucesso!")
        else:
            print("Produto ou loja não encontrados.")


