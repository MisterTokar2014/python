def factorio():
    player_inventory = {"железные руды": 0, "уголь": 0, "железные пластины": 0, "подшипники": 0}
    factory_inventory = {"железные руды": 100, "уголь": 50}
    
    print("Добро пожаловать в игру Factorio!\n")
    print("Ваша задача - развить свою фабрику и создать автоматизированное производство.\n")
    
    while True:
        print("1. Добыть железные руды")
        print("2. Добыть уголь")
        print("3. Создать железные пластины")
        print("4. Создать подшипники")
        print("5. Показать инвентарь")
        print("6. Выйти из игры")
        
        choice = input("\nВыберите действие: ")
        
        if choice == "1":
            player_inventory["железные руды"] += 10
            print("Вы добыли 10 железных руд!\n")
        elif choice == "2":
            player_inventory["уголь"] += 5
            print("Вы добыли 5 угля!\n")
        elif choice == "3":
            if player_inventory["железные руды"] >= 5:
                player_inventory["железные руды"] -= 5
                player_inventory["железные пластины"] += 1
                print("Вы создали 1 железную пластину!\n")
            else:
                print("Недостаточно железных руд!\n")
        elif choice == "4":
            if player_inventory["железные пластины"] >= 2 and player_inventory["уголь"] >= 1:
                player_inventory["железные пластины"] -= 2
                player_inventory["уголь"] -= 1
                player_inventory["подшипники"] += 1
                print("Вы создали 1 подшипник!\n")
            else:
                print("Недостаточно ресурсов!\n")
        elif choice == "5":
            print("\nВаш инвентарь:")
            for item, count in player_inventory.items():
                print(f"{item}: {count}")
            print()
        elif choice == "6":
            print("\nСпасибо за игру! До свидания!")
            break
        else:
            print("\nВыберите корректное действие!\n")
        input("Нажмите Enter, чтобы продолжить ")

factorio()
