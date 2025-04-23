
class Item:
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def __repr__(self) -> str:
        return f"Smartphone({self.name})\nQuantity remaining: {self.quantity}"

    def Total_price(self):
        return self.quantity * self.price

class Smartphones(Item):
    def __init__(self, name, quantity, price, model: str):
        super().__init__(name, quantity, price)
        self.model = model

phone1 = Smartphones('samsung', 34, 600, 'S22')

print(phone1.Total_price())

