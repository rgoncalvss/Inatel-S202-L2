from database import Database
from menu import Menu

def main():
    db = Database("bolt://100.24.3.219:7687", "neo4j", "abbreviations-fuels-star")
    #db.drop_all()

    menu = Menu(db)
    menu.exibir_menu()

if __name__ == "__main__":
    main()
