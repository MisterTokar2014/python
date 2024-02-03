from constants import *
from order import *
from order import*
def choise_pizza():
    print('Добро пожаловать в пиццерию пицца дрим')
    print("Меню пиццерии")
    for i, pizza in enumerate(PIZZA):
        print(f'{i+1}.{pizza} - {COST[i]} рублей')
    while True:
        order = int(input("выберете свою пиццу"))
        order -= 1
        get_order(order_pizza=order)
        
        
        print("Пицца добавлена в корзину")
        flag = input("хотите продолжить заказывать?")
        if flag.upper() == 'НЕТ':
            print("вы вышли из меню")
            break
        
choise_pizza()