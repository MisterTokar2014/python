<<<<<<< HEAD

def  plus(x, y):
    return x + y
def  minus(x, y):
    return x - y
def  delit(x, y):
    return x / y
def  umnohit(x, y):
    return(x * y)
=======
def rain:
    name = input("введите ваше имя ")
    def  plus(x, y):
        return x + y
    def  minus(x, y):
        return x - y
    def  delit(x, y):
        return x / y
    def  umnohit(x, y):
        return(x * y)
>>>>>>> b1dc623a9604ba3ecb6e478338d5023377b9fc11


def input_number(input_frese):
    x=input(input_frese)
    if not y.isdigit():
        print("вводить можно только числа")
        return input_number(input_frese)
    return int(x)

def main(name):
    while True:
        d = int(input(f"{name} введите 1 число "))
        if not x.isdigit():
            print("вводить можно только числа")
            continue
        x = int(x)
        a= input(f"{name} введите знак действия или выход для выхода")
        u = int(input(f"{name} введите 2 число "))
        if not y.isdigit():
            print("вводить можно только числа")
            continue
        y = int(y)
        if a == '+':
            result = plus(d, u)
            print(f"ответ {result}") 
        elif a == '-':
            resul = minus(d, u)
            print(f"ответ {resul}")
        elif a == '*':
            resu = umnohit(d, u)
            print(f"ответ {resu}")
        elif a == ':':
            if u == 0:
                print("на ноль делить нельзя.")
            else:
                res = delit(d, u)
                print(f"ответ {res}")
        elif a == "выход":
            break             
