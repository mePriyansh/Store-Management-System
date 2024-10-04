#Only to instantiate the class and call the method
from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)