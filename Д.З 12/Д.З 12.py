class Car:
    def __init__(self, mark: str, bithy: str):
        self.mark = mark.capitalize()
        self.bithy = bithy
        self.speed = 100
        self.komfort = "79"
        self.stop = "остановилась"

    def harasteristiki(self):
        print(f"{self.mark} {self.bithy} уровня комфорта {self.komfort}% из 100 разгоняется до скорости {self.speed}km в час.")

    def speed_down(self):
        self.speed -= 50
        print(f"Скорость {self.mark} {self.bithy} упала до {self.speed}km в час")
        self.speed += 50

    def stopeshechki(self):
        self.speed -= 99
        print(f"Скорость {self.mark} {self.bithy} уменьшилась до {self.speed}km в час и {self.mark} {self.stop} ")
        self.speed += 99


car = Car(mark="Tesla", bithy="Model X")
car.harasteristiki()
car.speed_down()
car.stopeshechki()


class Son(Car):
    def __init__(self, mark: str, bithy: str, sport: int):
        super().__init__(mark, bithy)
        self.sport = sport

    def dispute(self):
        self.speed += 75
        super()
        print(f"{self.mark} {self.bithy} умеет ехать со скоростью {self.speed} km в час")
        self.speed -= 75


son = Son("Tesla", "Model Y", 23)
son.harasteristiki()
son.dispute()
son.stopeshechki()
