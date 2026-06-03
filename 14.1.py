# 14.1.py
from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"  - {flavor}")

ice_cream = IceCreamStand("Мороженка", "Кафе-мороженое", 
                          ["Ванильное", "Шоколадное", "Клубничное", "Фисташковое"])
ice_cream.describe_restaurant()
ice_cream.show_flavors()
