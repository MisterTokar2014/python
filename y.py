def sing_up():
    login = input('придумайте логин: ')
    password1 = input('придумайте пароль')
    password2 = input('введите пароль ещё-раз')
    if password1 == password2:
        write_to_file('logins.txt', login+'\n')
        write_to_file('passwords.txt', password1+"\n")
        print(f"Пользователь{login} успешно заригестрирован")
    else:
        print("пароли не схожи. Проверьте ещё раз иначе Капибара с мандарином взорвёт ваш компьютер")
        
        
        
        
        
def write_to_file(filename, text):
    with open('y', mode='a', encoding='UTF-8') as file:
        file.write()
        
        
        
while True:
    print('Это прграмма Капибара с мандарином, и вот что она умеет')
    print('1-зарегестрировоться')
    print('2-выйдти из программыы')
    acsh = input("введите номер действия:")
    if acsh == '1':
        sing_up()
    if acsh == '2':
        print("спасибо за использование программы Капибара с мандарином")
        break
    input("нажмите энтер, что-бы продолжить")