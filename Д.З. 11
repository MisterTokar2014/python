class PhraseDecorator:
    def decorate(self, phrase):
        line = '-' * (len(phrase) + 4)
        print(line)
        print('|', phrase, '|')
        print(line)


decorator = PhraseDecorator()
decorator.decorate('Я люблю ООП')



class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def start_engine(self):
        print(f"Двигатель автомобиля {self.brand} {self.model} {self.year} года заведен!")

    def accelerate(self, speed):
        print(f"Автомобиль {self.brand} {self.model} ускоряется до {speed} км/ч.")

    def stop(self):
        print(f"Автомобиль {self.brand} {self.model} остановлен.")


my_car = Car("Toyota", "Camry", "синий", 2024)
my_car.start_engine()
my_car.accelerate(100)
my_car.stop()
