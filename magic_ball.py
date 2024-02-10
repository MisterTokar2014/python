def main():
    import random
    while True:
        p = str(input())
        magic = ["да", "нет", "возможно", "скорее нет", "скорее да", "конечно", "я не знаю", "даже не думай", "думаю да", "думаю нет"]
        print(random.choice(magic))
        if p == "да":
            print("сбой системы")
            break
        if p == "нет":
            print("сбой системы")
            break
        if p == "возможно":
            print("сбой системы")
            break
        if p == "скорее нет":
            print("сбой системы")
            break
        if p == "скорее да":
            print("сбой системы")
            break
        if p == "конечно":
            print("сбой системы")
            break
        if p == "я не знаю":
            print("сбой системы")
            break
        if p == "":
            print("сбой системы")
            break
        if p == "даже не думай":
            print("сбой системы")
            break
        if p == "думаю да":
            print("сбой системы")
            break
        if p == "думаю нет":
            print("сбой системы")
            break
        if __name__ == "__name__":
            magic()
