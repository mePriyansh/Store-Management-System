class Item:
    def __init__(self, name: str, price: float ,quantity=0):
        #Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"
        
        #Assign to self object
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
