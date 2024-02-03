from constants import *
user_pizza = []
user_cost = []

def get_order(order_pizza):
    global user_pizza, user_cost
    user_pizza.append(PIZZA[order_pizza])
    user_cost.append(COST[order_pizza])