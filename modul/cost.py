from constants import *
from order import *

def show_cost():
    global user_pizza, user_cost
    print(f"вы заказали следуйщие пиццы")
    for number, pizza in enumerate(user_pizza):
        print(f"{number+1}. {pizza} - {user_cost[number]}")
    print("Общая стоимость заказа:")
    summa = sum(user_cost)
    print(summa)
    return summa