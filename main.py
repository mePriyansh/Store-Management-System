#Only to instantiate the class and call the method
from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)

item1=Item("Laptop", 100, 3)
item1.apply_increment(0.2)
print(item1.price)