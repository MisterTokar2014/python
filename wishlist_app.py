def main():
    print("Это приложение список желаний")
    name = input("Как к вам можно обращатся:")
    wishlist=[]
    while True:
        print(f"Меню:")
        print("1 - добавить желание")
        print("2 - показать все желания")
        print("3 - удалить  желание")
        action = input("Что хотите сделать ->")
        if action == "1":
            wish = input(f"{name}, какое желание хоите добавить:")
            if wish not in wishlist:
                wishlist.append(wish)
                    
        elif action == "2":
            for i, wish in enumerate(wishlist, start=1):
                print(f"{i}.{wish}")
        elif action == "3":
            for i, wish in enumerate(wishlist,start=1):
                print(f"{i}.{wish}")
            delete_index = input(f"{name},введите номер желания для удаления")
        input("Нажмите Enter, чтобы продолжить")
