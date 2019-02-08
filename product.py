
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def checkStock(self, quantity):
        if quantity <= self.quantity:
            return True

    def calculateTotalPrice(self, quantity):
        return quantity * self.price

    def updateQuantity(self, quantity):
        self.quantity=self.quantity - quantity

