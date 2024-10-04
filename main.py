class Item:
    pay_rate = 0.8 #Class attribute
    
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
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

print(Item.pay_rate) #To print the class attribute

item1=Item("Phone",100,5)
print(item1.__dict__) #To print all the attributes of the object 
item1.apply_discount()
print(item1.price)

item2=Item("Laptop",1000,3)
item2.pay_rate=0.7
print(item2.__dict__)
item2.apply_discount()
print(item2.price)