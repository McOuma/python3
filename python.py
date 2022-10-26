#class and object instantiation 
class Fruits():
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_cost(self):
        total_cost = self.price*self.quantity
        return total_cost

fruit_1 = Fruits("orange", 45, 67)
fruit_2 = Fruits("strawberry", 500, 45)
fruit_3 = Fruits("pawpaw", 450, 35)

print(fruit_1.total_cost())
print(fruit_2.total_cost())
print(fruit_1.name)
print(fruit_2.name)
print(fruit_3.name, fruit_3.price)



class Employee():
    def __init__(self, name, salary, department):
        self.name = name
        self.department = department
        self.salary = salary 
employee_1 = Employee("Amos", 150000, "Finance")
print(employee_1.name)





