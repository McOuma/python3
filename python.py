#print ('hello.py')
class Fruits():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_cost(self):
        return self.price*self.quantity

fruit_1 = Fruits("orange", 45, 67)
print(fruit_1.total_cost())
print(fruit_1.name)