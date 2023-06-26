class Product:
    def __init__(self, name, category, price, discount, quantity=0):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount
        self.quantity = quantity

    def calcular_preco_com_disconto(self):
        price_with_discount = self.price - (self.price * self.discount / 100)
        return price_with_discount

    def to_dict(self):
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'discount': self.discount,
            'quantity': self.quantity
        }
