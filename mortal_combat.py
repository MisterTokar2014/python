import random
class Fighter:
    def __init__(self, name:str, name_fatslity:str):
        self.name = name
        self.power = random.randint(1, 5)
        self.hp = 100
        self.name_fat = name_fatslity
        
filter1 = Fighter("Скорпион", "Скорпионья суператака")
filter2 = Fighter("Охладулькин", "сосульки-ударюльки")
filter3 = Fighter("Конг-фу панда", "Скидыщ")
filter4 = Fighter("Змея", "СССсссс...")
filter5 = Fighter("пульт от ядерки", "ББББббббббууууууууумммммм")

fighters = [filter1, filter2, filter3, filter4, filter5]
enumy1 = random.choice(fighters)
fighters.remove(enumy1)
enumy5 = random.choice(fighters)
fighters.append(enumy1)

print(f"{enumy1.name} vs {enumy5.name}")