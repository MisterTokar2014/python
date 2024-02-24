import random
class Fighter:
    def __init__(self, name:str, name_fatslity:str):
        self.name = name
        self.power = random.randint(1, 5)
        self.hp = 100
        self.name_fat = name_fatslity
        self.fat_switsh = True

    def attaka(self, attaced_fighter):
        if self.fat_switsh:
            self.fatality(attaced_fighter)
        attaced_fighter.hp -= self.power
        print(f"{self.name} наносит {self.power}ед. урона персонажу {attaced_fighter.name}")
        self.harakiri()
    
    

    def say_info(self):
        print(f"У персонажа {self.name} {self.hp} ед. здоровья")

    def fatality(self, attaced_fighter):
        if self.hp < 15:
            damage = random.randint(0, attaced_fighter.hp)
            attaced_fighter.hp -= damage
            print(f"{self.name} применяет суператаку {self.name_fat} и наносит {damage}ед. урона персонажу {attaced_fighter.name}")
            self.fat_switsh = False
            
    def harakiri(self):
        if self.hp < 5 and random.randint(1,2)==1:
            print(f"{self.name} совершил харакири")
            self.hp = 0
            



filter1 = Fighter("Скорпион", "Скорпионья суператака")
filter2 = Fighter("Охладулькин", "сосульки-ударюльки")
filter3 = Fighter("Конг-фу панда", "Скидыщ")
filter4 = Fighter("Змея", "СССсссс...")
filter5 = Fighter("пульт от ядерки", "ББББббббббуууууууууммммммшшшшшшшшшшшшшщщщщщщщ")

fighters = [filter1, filter2, filter3, filter4, filter5]
enumy1 = random.choice(fighters)
fighters.remove(enumy1)
enumy5 = random.choice(fighters)
fighters.append(enumy1)

print(f"{enumy1.name} vs {enumy5.name}")
while True:
    enumy1.attaka(enumy5)
    enumy5.attaka(enumy1)
    enumy1.say_info()
    enumy5.say_info()
    if enumy1.hp <= 0 and enumy5.hp <= 0:
        print("ничья")
        break
    if enumy5.hp <= 0:
        print(f'{enumy1.name.upper()} победил(а)')
        break
    if enumy1.hp <= 0:
        print(f'{enumy5.name.upper()} победил(а)')
        break
