class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price*self.quantity


item1=Item("Phone",100,5)
print(item1.name)
print(item1.price)
print(item1.quantity)  
print(item1.calculate_total_price())

item2=Item("Laptop",1000,3)
print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total_price())
