<<<<<<< HEAD
=======
from calculator import rain
from magic_ball import main
from cyberpunk_game import ain
from password_generator import sain
from wishlist_app import dain
from robotcraft import fain
from newyear import gain
import time
def sing_up():
    login = input("придумайте логин: ")
    password1 = input("придумайте пароль")
    password2 = input("введите пароль ещё-раз")
    if password1 == password2:
        write_to_file("logins.txt", login + "\n")
        write_to_file("passwords.txt", password1 + "\n")
        print(f"Пользователь{login} успешно заригестрирован")
    else:
        print("пароли не схожи. Проверьте ещё раз иначе Капибара с мандарином взорвёт ваш компьютер")
        time.sleep(4)
        print("что ждёшь?")
        time.sleep(4)
        print("выключение компьютера через")
        for i in range(3,1):
            time.sleep(2)       
            import os
            os.system("shutdown")


def sing_in():
    login = input("введите логин: ")
    password = input("введите пароль: ")
    login_list = read_list("logins.txt")
    password_list = read_list("passwords.txt")
    if login in login_list:  # если логин в списке логинов
        login_str = login_list.index(login)  # находим его индекс
        true_password = password_list[login_str]  # берём пароль с таким же индексом
        if password == true_password:
            print("вы успешно вошли в систему")
            return True
        else:
            print("пароль неправильный")
            return False
    else:
        print("пользователя с таким логином не существует")
        return False


def write_to_file(filename, text):
    with open(filename, mode="a", encoding="UTF-8") as file:
        file.write(text)


def read_list(filename):
    with open(filename, mode="r", encoding="UTF-8") as file:
        text = file.read().split("\n")
        return text


access = False
while True:
    if not access:
        print("Это прграмма Капибара с мандарином, и вот что она умеет")
        print("1-зарегестрироваться")
        print("2-войти в систему")
        print("3-выйдти из программыы")
        acsh = input("введите номер действия:")
        if acsh == "1":
            sing_up()
        elif acsh == "2":
            access = sing_in()

        if acsh == "3":
            print("спасибо за использование программы Капибара с мандарином")
            break
    elif access:
        print("Меню:")
        git = int(input("введите 1 что-бы запустить текстокрафт, введите 2 что-бы запустить магический шар, введите 3 что-бы запустить cyberpunk_2077, введите 4 что-бы запустить список желаний, введите 5 что-бы запустить новогоднюю игру, введите 6 что-бы запустить калькулятор, введите 7 что-бы запустить генератор паролей"))
        if git == "1":
            fain()
        if git == "2":
            main()
        if git == "3":
            ain()
        if git == "4":
            dain()
        if git == "5":
            gain()
        if git == "6":
            rain()
        if git == "7":
            sain()  
    input("нажмите энтер, что-бы продолжить")
>>>>>>> b1dc623a9604ba3ecb6e478338d5023377b9fc11
