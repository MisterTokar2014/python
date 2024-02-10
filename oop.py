class Marker:
    def __init__(self, color, firm, fat):
        self.color = color
        self.firm = firm
        self.fat = fat
        
    def write(self):
        print(f"маркер фирмы {self.firm} рисует")

    def say(self):
        print(f"Я маркер. Я {self.color}. Моя фирма {self.firm}. Моя толщина письма {self.fat} милиметров")
        
    
marker1 = Marker(color="чёрный", firm="Brauberg", fat = 5)
marker2 = Marker("красный", "Молотов", 10)
print(marker1.firm, marker1.color)
print(marker2.firm, marker2.color)
marker1.write()
marker1.say()

class Human:
    def __init__(self, name, surname, age, weight, growth):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.growth = growth
        
    def birthday(self):
        self.age += 1     
        print(f"С днём рождения тебя, {self.name, self.surname}! Тебе {self.age} лет")
vasua = Human("Костя", "Токарь", 9, 10,120)
