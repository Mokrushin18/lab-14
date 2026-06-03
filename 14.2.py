# 14.2.py
from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.location = location
        self.working_hours = working_hours
        self.flavors = []
        self.ice_cream_types = {
            "на палочке": [],
            "мягкое": [],
            "в стаканчике": [],
            "в рожке": []
        }
    
    def add_flavor(self, flavor, ice_type="в стаканчике"):
        if ice_type in self.ice_cream_types:
            self.flavors.append(flavor)
            self.ice_cream_types[ice_type].append(flavor)
            print(f"Добавлен сорт '{flavor}' ({ice_type})")
        else:
            print("Неверный тип мороженого")
    
    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            for ice_type in self.ice_cream_types:
                if flavor in self.ice_cream_types[ice_type]:
                    self.ice_cream_types[ice_type].remove(flavor)
            print(f"Удален сорт '{flavor}'")
        else:
            print(f"Сорт '{flavor}' не найден")
    
    def has_flavor(self, flavor):
        return flavor in self.flavors
    
    def show_flavors_by_type(self, ice_type=None):
        if ice_type:
            if ice_type in self.ice_cream_types:
                print(f"Мороженое {ice_type}: {', '.join(self.ice_cream_types[ice_type])}")
            else:
                print("Неверный тип")
        else:
            for ice_type, flavors in self.ice_cream_types.items():
                print(f"{ice_type}: {', '.join(flavors)}")
    
    def describe_restaurant(self):
        super().describe_restaurant()
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.working_hours}")

ice = IceCreamStand("Мороженка", "Кафе-мороженое", 
                   "ТЦ 'Галерея'", "10:00-22:00")
ice.add_flavor("Ванильное", "в рожке")
ice.add_flavor("Шоколадное", "мягкое")
ice.add_flavor("Клубничное", "на палочке")
ice.add_flavor("Фисташковое", "в стаканчике")

ice.describe_restaurant()
print()
ice.show_flavors_by_type()
print(f"Есть ванильное? {ice.has_flavor('Ванильное')}")
ice.remove_flavor("Клубничное")
ice.show_flavors_by_type()
