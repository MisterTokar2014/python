PIZZA = ["Маргаррита", "Пепперони", "4 сыра", "Гавайская"]
COST = [550, 675, 700, 850]
user_pizza = []
user_cost = []

def choise_pizza():
    print('Добро пожаловать в пиццерию пицца дрим')
    print("Меню пиццерии")
    for i, pizza in enumerate(PIZZA):
        print(f'{i+1}.{pizza} - {COST[i]} рублей')
    while True:
        order = int(input("выберете свою пиццу"))
        user_pizza.append(PIZZA[order-1])
        user_cost.append(COST[order-1])
        print("Пицц добавлена в корзину")
        flag = input("хотите продолжить заказывать?")
        if flag.upper() == 'Нет':
            print("вы вышли из меню")
            break