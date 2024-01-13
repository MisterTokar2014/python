# 20 (что-то новогоднее)
import webbrowser
print("До нового года остался 1 день")
# webbrowser.open_new_tab('https://img.freepik.com/free-vector/2024-happy-new-year-happy-new-year-banner-with-numbers-date-2022-dark-background-vector-illustration_145391-1462.jpg?size=626&ext=jpg&ga=GA1.1.1546980028.1704326400&semt=ais')
y = input("какой квест вы хотите выбрать(1,2,3 или 4)")
if y == "1":
    s = input('ваши действия(1-построить ёлочку, 2-я не могу это описать)')
    if s == '1':
        def draw_tree(height):
            for i in range(height):
                print(' ' * (height - i - 1) + '*' * (2 * i + 1))
            print(' ' * (height - 1) + '|')


        tree_height = int(input('Введите высоту ёлочки: '))
        draw_tree(tree_height)

    elif s == '2':
        import random


        def steal_presents():
            presents = ["игрушка", "конфеты", "новогодняя открытка", "шоколадный букет", "компьютерная игра"]
            stolen_present = random.choice(presents)
            return stolen_present


        def steal_sleigh():
            if random.random() < 0.5:
                return True
            else:
                return False


        def main():
            print("Добро пожаловать в новогоднюю игру!")
            print("У вас есть шанс украсть подарки и угнать сани деда Мороза.")
            print("Если у вас это получится, дед Мороз даст вам угольки на новый год!")
            print()

            choice = input("Вы хотите украсть подарки? (да/нет) ")

            if choice.lower() == "да":
                stolen_present = steal_presents()
                print(f"Вы украли: {stolen_present}!")
            else:
                print("Вы решили не рисковать и оставить подарки в покое.")

            choice = input("Вы хотите угнать сани деда Мороза? (да/нет) ")

            if choice.lower() == "да":
                if steal_sleigh():
                    print("У вас получилось угнать сани!")
                    print("Дед Мороз теперь будет обходить новогодние дома пешком.")
                else:
                    print("К сожалению, попытка угнать сани деда Мороза не удалась.")
            else:
                print("Вы решили не рисковать и оставить сани в покое.")

            print()
            print("Спасибо за игру!")
            print("Дед Мороз пожелал вам счастливого нового года и оставил вам угольки.")
            print("Наслаждайтесь праздником!")


        if __name__ == "__main__":
            main()
elif y == '2':

    import random

    def start_game():
        name = input("Добро пожаловать в новогодний квест! Представьтесь, пожалуйста: ")
        print(f"Привет, {name}! Ваша задача - найти потерянные подарки Санта Клауса.")
        print("Вас ждут различные испытания и загадки. Удачи!")

        current_room = "начальная комната"
        items = []

        while True:
            if current_room == "начальная комната":
                print("Вы находитесь в начальной комнате.")
                print("Пора начинать свой путь!")
                print("1. Искать подарки")
                print("2. Покинуть комнату")
                choice = input("Выберите действие: ")

                if choice == "1":
                    if "ключи" in items:
                        print("Вы уже нашли все подарки.")
                    else:
                        print("Вы нашли ключи! Теперь вы можете открыть другие комнаты.")
                        items.append("ключи")
                elif choice == "2" and "ключи" in items:
                    print("Вы покинули комнату.")
                    current_room = "комната с головоломкой"
                elif choice == "2":
                    print("У вас нет ключей, поэтому не получается выйти")
                else:
                    print("Некорректный выбор. Попробуйте еще раз.")

            elif current_room == "комната с головоломкой":
                print("Вы зашли в комнату с головоломкой.")
                print("Перед вами стоит три ящика.")
                print("В одном из ящиков находится подарок.")
                print("Выберите ящик для открытия.")
                print("1. Ящик №1")
                print("2. Ящик №2")
                print("3. Ящик №3")
                choice = input("Выберите ящик: ")

                if choice == str(random.randint(1, 3)):
                    print("Поздравляю, вы нашли подарок!")
                    items.append("подарок")
                    current_room = "выход"
                else:
                    print("Увы, в этом ящике подарка нет.")

            elif current_room == "выход":
                print("Вы успешно нашли все подарки!")
                print("С наступающим Новым Годом!")

                play_again = input("Хотите сыграть еще раз? (да/нет): ")
                if play_again.lower() == "да":
                    start_game()
                else:
                    print("Спасибо за игру!")
                    break

    start_game()
elif y == '3':
    import random


    def start_game():
        print("Добро пожаловать в новогодний квест!")
        print("Вы - герой, который должен найти потерянные подарки Деда Мороза.")
        print("Однако, если вы не вели себя хорошо, Дед Мороз подарит вам угольки.")
        print("Удачи!")

        gifts = ["игрушечный автомобиль", "книга", "мяч", "конструктор", "космический корабль"]
        coal = ["уголька", "угольки", "угольков"]
        found_gifts = []
        found_coal = []

        naughty = False

        while len(found_gifts) < len(gifts):
            if naughty:
                print("О нет! Вы плохо себя вели...")
                print("Дед Мороз дарит вам угольки.")
                found_coal.append(random.choice(coal))
            else:
                print("Выберите следующую комнату для поиска подарка:")
                print("1. Гостиная")
                print("2. Спальня")
                print("3. Кухня")
                choice = input("Выберите комнату: ")

                if choice in "123":
                    gift = random.choice(gifts)
                    print(f"Вы нашли подарок {gift} в гостиной!")
                    found_gifts.append(gift)
                else:
                    print("Некорректный выбор. Попробуйте еще раз.")

            naughty = random.choice([True, False])

        print("Поздравляем!")
        print("Вы нашли все подарки Деда Мороза.")
        print("Вот ваши подарки:")
        for gift in found_gifts:
            print("- " + gift)

        if len(found_coal) > 0:
            print("И увы, Дед Мороз подарил вам немного угольков:")
            for c in found_coal:
                print("- " + c)

        print("Наслаждайтесь вашими подарками!")


    start_game()
elif y == '4':
    print("вы попали в симулятор деда Мороза")
    def play_game():
        milk_and_cookies = input("Дед Мороз, дали ли вам дети молочко и печенье? (да/нет): ")

        presents = 10  # Начальное количество подарков

        if milk_and_cookies.lower() == "да":
            print("Спасибо детишкам за молочко и печенье! Вот ваши подарки!")
        else:
            print("Эх, дети не оставили молочко и печенье...")
            print("Дед Мороз(вы) оставили им записку и подарили на 1 подарок меньше.")
            presents -= 1

        print(f"У вас осталось {presents} подарков.")
        print("Дед Мороз(вы) желаете всем счастливого Нового Года!")


    play_game()