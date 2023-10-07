salary = 6900
veg_sale = 0.7#70 процентов
cucumbers = 90
tomato = 150
strawberry = 385
cookie = 140 + 140
#умножение на veg_sale- это овощи со скидкой
buy = (cucumbers * 5  + tomato * 4) * veg_sale + cookie
print(f"у таксиста Вани из {salary} после траты {buy} рублей осталось {salary - buy} рублей")

print(10//3)# целочисленое деление
print(10%3)#остаток от деления
left = salary - buy
stock = 134.65
travel = 36
print(f"Таксист Ваня сможет купить {left // stock} акций")
print(f"У таксиста Вани остаётся {int(left % stock)} рублей, проезд стоит {travel} рублей")

number = int (input("Введите число: "))
first = number // 100
second = number // 10 % 10
third = number % 10
print(third + second + first)
