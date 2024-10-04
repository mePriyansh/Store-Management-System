import csv

class Item:
    pay_rate = 0.8 #Class attribute
    all=[]
    
    def __init__(self, name: str, price: float ,quantity=0):
        #Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
            
    @staticmethod
    def is_integer(num):
        #We will count out the floats that are point zero
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        return False
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
class Phone(Item):
    all=[]
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #Call to super function to have access to all attributes
        super().__init__(name, price, quantity)
        #Run validation to the received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to 0"
        
        #Assign to self object
        self.broken_phones = broken_phones
        
        Phone.all.append(self)

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(1.0))

phone1 = Phone('iPhone 12', 1000, 5, 1)
print(Phone.all)
print(phone1.calculate_total_price())