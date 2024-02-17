class Father:
    def __init__(self,name:str, age:int):
        self.name = name.capitalize()
        self.age = age
        self.gender = "мужчина" 
        self.power = 0
        

    def swim(self):
        print(f"{self.name} плавает брассом")

    def dispute(self):
        print(f"{self.name} спорит басом" )

    def chopping(self):
        self.power += 1
        print(f"{self.name} рубит дрова. Сила = {self.power}")
father = Father(name="Олег", age=55)
father.swim()
father.dispute()
father.chopping()


class Son(Father):
    def __init__(self, name: str, age: int, sport:int):
        super().__init__(name, age)
        self.sport = sport
        
    def dispute(self):
        super().dispute()
        print(f"{self.name} спорит")


son = Son("Роман", 5, 23)
son.swim()
son.dispute()
son.chopping()
