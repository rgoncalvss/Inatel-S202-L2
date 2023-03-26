from database import Database
from save_json import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

class ProductAnalyzer:

    def customer_b_total_spent(self):
        pipeline = [
            {'$match': {'cliente_id': 'B'}},
            {'$unwind': '$produtos'},
            {'$group': {'_id': None, 'total_spent': {'$sum': {'$multiply': ['$produtos.quantidade', '$produtos.preco']}}}}
        ]
        result = list(db.collection.aggregate(pipeline))
        if len(result) > 0:
            return writeAJson(result[0]['total_spent'], "gastos_clliente_B")
        else:
            return 0

    def least_sold_product(self):
        pipeline = [
            {'$unwind': '$produtos'},
            {'$group': {'_id': '$produtos.nome', 'total_sold': {'$sum': '$produtos.quantidade'}}},
            {'$sort': {'total_sold': 1}},
            {'$limit': 1}
        ]
        result = list(db.collection.aggregate(pipeline))
        if len(result) > 0:
            return writeAJson(result[0]['_id'], "menos_vendido")
        else:
            return ''

    def least_spent_customer(self):
        pipeline = [
            {'$unwind': '$produtos'},
            {'$group': {'_id': '$_id', 'min_spent': {'$min': {'$multiply': ['$produtos.quantidade', '$produtos.preco']}}}},
            {'$sort': {'min_spent': 1}},
            {'$limit': 1}
        ]
        result = list(db.collection.aggregate(pipeline))
        if len(result) > 0:
            return writeAJson(result[0]['_id'], "menos_gastou")
        else:
            return ''

    def products_sold_above_2_units(self):
        pipeline = [
            {'$unwind': '$produtos'},
            {'$match': {'produtos.quantidade': {'$gt': 2}}},
            {'$group': {'_id': '$produtos.nome'}}
        ]
        result = list(db.collection.aggregate(pipeline))
        if len(result) > 0:
            return writeAJson([item['_id'] for item in result], "vendidos_acima_de_2")
        else:
            return []


