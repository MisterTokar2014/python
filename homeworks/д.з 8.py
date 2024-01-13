def minus(x, y):
    return x - y


let = 2023
vos = int(input("введите ваш возраст:"))
print(minus(let, vos))
chislo = int(input("введите 1 число"))
chisla = int(input("введите 2 число"))
chisly = int(input("введите 3 число"))
u_7 = [chisly, chisla, chislo]
u_7.sort(reverse=True)
print(f'Максимальный элемент в списке: {u_7[0]}')


def summa_chisel(num1, num2):
    summa = 0
    for num in range(num1, num2 + 1):
        print(num)
        summa += num
    return summa


number = int(input("Введите первое число: "))
yomber = int(input("Введите второе число: "))
res = summa_chisel(number, yomber)
print("Сумма чисел между", number, "и", yomber, "равна", res)
