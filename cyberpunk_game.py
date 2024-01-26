def ain():
    n = 0
    import time
    import webbrowser
    print("Дисклеймер: я никогда не играл в cyberpunk 2077")
    j = []

    i = input('вы попали в cyberpunk 2024(или 2077) вы хотите начать?("да" или "нет")')
    if i == "да":
        print("как только вы начали вы увидели это")
        webbrowser.open_new_tab('https://playinfo.net/wp-content/uploads/2020/11/1-99.jpg')
        time.sleep(1)
        my = input('круто?("да" или "нет")')
        if my == "нет":
            print("я так долго искал как открыть изображение в среде программирования")
            exit()
        else:
            print("спасибо")
            print("ну а теперь приступим к делаам")
            while True:
                d = input(" введите 1 если хотите сыграть в казино\n введите 2 если хотите в Турцию\n введите 3 если хотите ограбить банк\n введите 4 если хотите открыть калькулятор\n введите 5 что-бы пойдти в магазин\n введите 6 что-бы устоиться на работу\n введите 7  что-бы узнать ваш баланс\n введите 8, что-бы узнать что вы купили")
                if d == '1':
                    print("правила: В начале каждого раунда вы делаете ставку, а затем бросаете две кости. Если сумма выпавших чисел равна 7, вы выигрываете и увеличиваете свой баланс, в противном случае вы проигрываете и уменьшаете свой баланс. Игра продолжается до тех пор, пока у вас есть средства для ставок.")
                    import random
                    def roll_dice():
                        dice1 = random.randint(1, 6)
                        dice2 = random.randint(1, 6)
                        return dice1 + dice2
                    def play_game():
                        money = 100
                        while money > 0:
                            print(f"Ваш баланс: {money}")
                            bet = int(input("Сделайте ставку: "))
                            if bet > money:
                                print("У вас недостаточно средств.")
                                continue
                            dice_result = roll_dice()
                            print(f"Выпало {dice_result}")
                            if dice_result == 7:
                                money += bet
                                print(f"Вы выиграли {bet}! Ваш баланс теперь составляет {money}")
                            else:
                                money -= bet
                                print(f"Вы проиграли {bet}. Ваш баланс теперь составляет {money}")
                        print("Игра закончена. У вас закончились средства.")
                    play_game()
                elif d == "2":
                    webbrowser.open_new_tab('https://zvukogram.com/category/zvuki-shum-morya-voln-i-kriki-chaek/')
                    print(" Ты побыл в Турции и хорошо отдохнул\n ну а теперь домой")
                elif d == '3':
                    print("вы приехали в банк")
                    m = input('ваши действия:("нажмите 1 что-бы не ограблять банк и пройдти мимо", "нажмите 2 что-бы устоить перестрелку и ограбить банк(рядом стоит полицейская машина)", "нажмите 3 что-бы просто войдти в банк и постоять около банкомата")')
                    if m == '1':
                        print("вы просто прошли мимо...")
                    elif m == '2':
                        print("вы устроили перестелку, менеджер показал вам где сейф, но если-бы не полицейская машина поблизости...У вас бы всё получилось\n но вам дали пожизненный срок... ")
                        exit()
                    elif m == '3':
                        print("вы зашли в банк и увидели код от сейфа, по если от него отвернуться, то он пропадёт")
                        webbrowser.open_new_tab('https://avatars.mds.yandex.net/i?id=34d2e1ad027339e65b3a32b849b53b98-7065781-images-thumbs&n=13')
                        time.sleep(5)
                        x = input("введите пароль")
                        if x == '1234':
                            print("вы выйграли 100000 ED")
                            n += 100000
                        else:
                            print("пароль неверный, вы начали убегать от полиции и хорошо, что убежали")
                elif d == '7':
                    print(f"ваш баланс составляет {n} ED ")
                elif d == '4':
                    def get_num():
                        return float(input("Введите число: "))
                    def get_operator():
                        return input("Введите оператор (+, -, *, /): ")
                    def calculate(x, y, operator):
                        if operator == '+':
                            return x + y
                        elif operator == '-':
                            return x - y
                        elif operator == '*':
                            return x * y
                        else:
                            return int(x / y) if y != 0 else 0
                    def main():
                        x = get_num()
                        operator = get_operator()
                        y = get_num()
                        result = calculate(x, y, operator)

                        print("Результат:", result)
                    if __name__ == "__main__":
                        main()
                elif d == '5':
                    print("                     Магазин")
                    print("--------------------------------------------------------------")
                    t = int(input(' "введите 1, что-бы купить телефон(5793 ED)", "введите 2, что-бы купить машину"(16796 ED)","введите 3, что-бы купить дом(21762 ED)" '))
                    if t == '1':
                        if n > 5793:
                            print("вы купили телефон.")
                            n -= 5793
                            j.append("телефон")
                        else:
                            print("недостаточно средств")
                    elif t == '2':
                        if n > 16796:
                            print("вы купили машину.")
                            n -= 16769
                            j.append("машинa")
                        else:
                            print("недостаточно средств")
                    elif t == '3':
                        if n > 21762:
                            print("вы купили дом.")
                            n -= 21762
                            j.append("дом")
                        else:
                            print("недостаточно средств")
                elif d == 6:
                    print("вы устроились на работу(вы будете получать зарплату)")
                    while True:
                        n += 100
                        time.sleep(1)
                        n += 100
                        print(n)
                        print("ой! Бизнес оборвался")
                        continue
    else:
        print("ну раз нет, то прощай приятель...")
        print("значит ты не хотел посмотреть на это:")
        webbrowser.open_new_tab('https://playinfo.net/wp-content/uploads/2020/11/1-99.jpg')
        print("и делать остальное...")
