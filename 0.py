import random
def get_one_world(filename):
    with open(filename, mode="r", encoding="UTF-8") as file:
        text = file.read().split("\n")
        return random.choice(text)
    
pr = get_one_world("pr.txt")
name = get_one_world("an.txt")
print(f"вас бы звали {pr} {name}")
