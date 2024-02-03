from cost import *
import random

def pay():
    money = random.choice(["да","нет"])
    if money == "да":
        print("вы оплатили ваш заказ ")
    else:
        print("вам не хватило денег")
