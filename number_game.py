import random
print("Это игра - угадай число.")
print("Тебе нужно угадать число от 1 до 100")
name = input("Как тебя зовут?")
game_round = 0
while game_round < 3:
    game_round+=1
    print(f"раунд №{game_round}")
    attempts = 1
    secret_number = random.randint(1, 100)
    while attempts <= 10:
        print(f"{name}, у вас попытка №{attempts}")
        user_number = input(f"{name}, Введи число")
        if not user_number.isdigit():
            print(f"{name}, вы ввели не число")
            continue
        attempts += 1
        user_number= int(user_number)
        print(name, "ты ввёл число", user_number)
        if secret_number > user_number:
            print("Моё число больше")
        elif secret_number < user_number:
            print("Моё число меньше")
        elif secret_number== user_number:
            print(name, "ты угадал моё число!")
            break
        print()
        if attempts == 10:
            print("все попытки кончились, вы не угадали")