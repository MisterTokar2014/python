def main():
    
    import random
    inventory = []
    def gaw():
        print("Гав-Гав-гав!")
    def robot_forward():
        print("Робот идёт вперёд")
    def robot_backward():
        print("Робот идёт назад")
    def robot_left():
        print("Робот идёт влево") 
    def robot_right():
        print("Робот идёт вправо")
    def robot_scan():
        items = ["Ветка", "бутылка", "железо", "дерево","лев", "летающая тарелка", "носорог", "бургер", "алмаз", "золото"]
        item = random.choice(items)
        print(f"Робот нашёл предмет {item}")
        return item
    def robot_pickup(item):
        global inventory
        inventory.append(item)
        

        
    def check_inventory():
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
    def craft():
        recept1 = ["золото","золото","золото",]#золотой слиток
        recept2 = ["золотой слиток", "ветка", "железо"]#золотой меч
        recept5 = ["алмаз", "алмаз"]#бриллиант
        recept3 = ["бриллиант", "золотой слиток", "палка"]#алмазный меч
        recept4 = ["золотой меч", "алмазный меч", "золотой слиток"]#супер оружие
        recepts = [recept1,recept2,recept3, recept4, recept5]#все рецепты
        recept_names = ["золотой слиток", "золотой меч","алмазный меч", "супер оружие", "бриллиант"]
        print("доступны следуйщие рецепты")
        for index, recept in enumerate(recept_names, start=1):
            print(f"{index}. {recept}")
        choice = input("выбери, что хочешь крафтить:")
        if not choice.isdigit():
            print("вводить можно только числа")
            return None
        choice = int(choice) - 1
        if choice not in range(0,len(recept_names)):
            print("рецепта с таким номером нет")
            return None
        choice_recept = recept_names[choice]
        print(f"вы выбрали крафтить {choice_recept}")
        ingredients = recept[choice]
        print(f"ингредиенты {ingredients}")
        for item in inventory:
            if item in ingredients:
                print(f"уничтожен {item}")
                inventory.remove(item)
                ingredients.remove(item)
        if not ingredients:
            inventory.append(choice_recept)
            print(f"в инвентарь добавлен{choice_recept}")
        else:
            print("не хватает ингредиентов")

        

    while True:
        key = input("Введите клавишу:")
        if key == "w":
            robot_forward()
        elif key == "s":
            robot_backward()
        elif key == "a":
            robot_left()
        elif key == "d":
            robot_right()
        elif key == "f":
            item = robot_scan()
            robot_pickup(item)
        elif key == "e":
            check_inventory()
        elif key == "c":
            craft()
    
            
    

            


