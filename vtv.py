'''for counter in range(100, 501, 50):
    print(counter)
    
for buy in ["яйца","молоко","лосось","доширак","масло","apple 15 pro max (x9999999999)"]:
    print(buy)
    print("This is Ilon Mask.")'''
todo_list = [
    "Разморозить курицу",
    "Сходить в магазин",
    "Купить телефон",
    "Сходить в спортзал",
    "Поиграть в маинкрафт",
    "Сходить на программирование"
]
todo_list.append("Покушать")
todo_list.insert(0, "Погулять")
todo_list.remove("Погулять")
todo_list.pop(4)

for todo in todo_list:
    print(todo)
