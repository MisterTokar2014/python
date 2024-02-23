class Item:
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe

    def __str__(self):
        return self.name


class Recipe:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output


class Factory:
    def __init__(self):
        self.inventory = {}
        self.recipes = {}

    def add_item(self, item):
        self.inventory[item.name] = 0
        self.recipes[item.name] = item.recipe

    def craft(self, item):
        if item not in self.recipes:
            print("Такой предмет нельзя создать!")
            return

        recipe = self.recipes[item]
        for required_item in recipe.inputs:
            if self.inventory[required_item] < recipe.inputs[required_item]:
                print(f"Недостаточно ресурса: {required_item}")
                return

        for required_item in recipe.inputs:
            self.inventory[required_item] -= recipe.inputs[required_item]

        self.inventory[item] += recipe.output

        print(f"Вы создали {recipe.output} {item}!")

    def print_inventory(self):
        print("\nВаш инвентарь:")
        for item, count in self.inventory.items():
            if count > 0:
                print(f"{item}: {count}")


# Создаем предметы и рецепты
iron_ore = Item("Железная руда", Recipe({}, 10))
iron_plate = Item("Железная пластина", Recipe({"Железная руда": 5}, 1))
gear = Item("Шестеренка", Recipe({"Железная пластина": 2}, 1))

# Создаем фабрику
factory = Factory()
factory.add_item(iron_ore)
factory.add_item(iron_plate)
factory.add_item(gear)

print("Добро пожаловать в игру Factorio!\n")
print("Ваша задача - развить свою фабрику и создать автоматизированное производство.\n")

while True:
    print("1. Добывать ресурс")
    print("2. Создавать предмет")
    print("3. Показать инвентарь")
    print("4. Выйти из игры")

    choice = input("\nВыберите действие: ")

    if choice == "1":
        resource = input("Введите название ресурса: ")
        if resource in factory.inventory:
            factory.inventory[resource] += 1
            print("Вы добыли ресурс!")
        else:
            print("Такой ресурс не существует!")
    elif choice == "2":
        item = input("Введите название предмета: ")
        factory.craft(item)
    elif choice == "3":
        factory.print_inventory()
    elif choice == "4":
        break
    else:
        print("Неверный выбор действия.")
