import time
import random

class Fighter:
    def __init__(self, name: str, name_fatslity: str):
        self.name = name
        self.power = random.randint(1, 5)
        self.hp = 100
        self.name_fat = name_fatslity
        self.fat_switsh = True
        

    def attaka(self, attaced_fighter):
        if self.fat_switsh:
            self.fatality(attaced_fighter)
        attaced_fighter.hp -= self.power
        self.power = random.randint(0, 5)
        if self.power == 0:
            print(f"{self.name} промахнулся(ась) и не нанёс(ла) урон персонажу {attaced_fighter.name}")
        print(f"{self.name} наносит {self.power}ед. урона персонажу {attaced_fighter.name}")
        self.harakiri()

    def say_info(self):
        print(f"У персонажа {self.name} {self.hp} ед. здоровья")

    def sobytye(self):
        sobities = ["падение метиорита", "восстановление жизней"] + ["ничего" ] * 3
        sobitie = random.choice(sobities)
        if sobitie == "падение метиорита":
            self.hp -= 20
            print("упал метеорит")
        if sobitie == "ничего"*3:
            print("ничего не произошло")
        if sobitie == "восстановление жизней":
            self.hp = 100

    def fatality(self, attaced_fighter):
        if self.hp < 15:
            damage = random.randint(0, attaced_fighter.hp)
            attaced_fighter.hp -= damage
            print(f"{self.name} применяет суператаку {self.name_fat} и наносит {damage}ед. урона персонажу {attaced_fighter.name}")
            self.fat_switsh = False

    def harakiri(self):
        if self.hp < 5 and random.randint(1, 2) == 1:
            print(f"{self.name} совершил харакири")
            self.hp = 0
    
    def golod(self, folod, enumy1):
        folod = 100
        u = random.choice(["яблоко", "палка", "уголь"])
        а = input("вы хотите поесть? да или нет?")
        if a  == "да":
            if u == "яблоко":
                print("вы поели")
                folod+=10
            if folod > 100:
                self.folod = 100
            if folod <= 0:
                print("вы истощены")
                exit()


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
def suget(self):
    print(f"История начинается в мире Земли, который оказывается под угрозой со стороны зловещего императора Властелина тьмы.\n Правитель Земли, Рейден, собирает команду боевых мастеров, чтобы сражаться против Властелина тьмы и его приспешников.\n Каждый боец имеет свою собственную мотивацию и цель в этой битве.\nВ ходе сюжета раскрывается множество интриг, предательств и разоблачений.\n Бойцы сражаются не только за спасение мира, но и за свою собственную судьбу.\n Открываются новые миры и измерения, и в каждом из них наши герои сталкиваются с новыми угрозами и опасностями.\nСюжет Мортал Комбат охватывает не только ожесточенные бои, но и духовную сторону боец.\n Некоторые из них обладают особыми способностями, связанными с магией, элементами природы или духовным наследием.\n Эти бои исследуют свои прошлые ошибки, находят внутреннюю силу и становятся теми, кем они предначертаны быть.\nВ конечном итоге, после многочисленных битв и преград, команда героев сражается лицом к лицу с Властелином тьмы.\n В эпической битве они сталкиваются со страшной силой и используют все свои навыки и способности, чтобы обуздать его.")
suget(self=None)
print(f"{enumy1.name} vs {enumy5.name}")
print("1 раунд")
raund = 1
while True:
    enumy1.attaka(enumy5)
    enumy5.attaka(enumy1)
    enumy1.say_info()
    enumy5.say_info()
    enumy1.sobytye()
    enumy5.sobytye()
    enumy1.golod()
    raund += 1
    time.sleep(1.5)
    print(f"{raund} раунд")
    if enumy1.hp <= 0 and enumy5.hp <= 0:
        print("ничья")
        break
    if enumy5.hp <= 0:
        print(f'{enumy1.name.upper()} победил(а)')
        break
    if enumy1.hp <= 0:
        print(f'{enumy5.name.upper()} победил(а)')
        break
