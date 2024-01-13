import random
p_9 = ["apple", "tree", "home", "glasses", "car", "lamp", "pen", "ruler", "pencil", "chair", "postman", "policeman", "robot", "lorry", "bus", "box", "sun", "Apple", "Tree", "Home", "Glasses", "Car", "Lamp", "Pen", "Ruler", "Pencil", "Chair", "Postman", "Policeman", "Robot", "Lorry", "Bus", "Box", "Sun", "apPle", "trEe", "hOme", "glasSes", "cAr", "lAmp", "pEn", "ruLer", "pEncil", "chaIr", "pOstman", "policEman", "rObot", "loRry", "buS", "bOx", "suN"]
om = ["apple", "tree", "home", "glasses", "car", "lamp", "pen", "ruler", "pencil", "chair", "postman", "policeman", "robot", "lorry", "bus", "box", "sun"]
prepinanie = [",", "!", "?", ".", ":", "...", ";", "-", "--", "()"]
todo_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
u_k = ["Apple", "Tree", "Home", "Glasses", "Car", "Lamp", "Pen", "Ruler", "Pencil", "Chair", "Postman", "Policeman", "Robot", "Lorry", "Bus", "Box", "Sun", "apPle", "trEe", "hOme", "glasSes", "cAr", "lAmp", "pEn", "ruLer", "pEncil", "chaIr", "pOstman", "policEman", "rObot", "loRry", "buS", "bOx", "suN"]
h = input("что вы хотите добавить в пароль ")
if h == "слова":
    print(random.choice(u_k))
elif h == "любое":
    print(random.choice(p_9)+random.choice(todo_list)+random.choice(p_9)+random.choice(prepinanie))
elif h == "слова, заглавные буквы, числа":
    print(random.choice(u_k)+random.choice(todo_list)+random.choice(om))
elif h == "слова, числа":
    print(random.choice(om)+random.choice(todo_list)+random.choice(om))
elif h == "числа":
    print(random.choice(todo_list))
if h == "слова, знаки препинания":
    print(random.choice(u_k)+random.choice(prepinanie))
elif h == "слова, заглавные буквы, числа, знаки препинания":
    print(random.choice(u_k)+random.choice(todo_list)+random.choice(om)+random.choice(prepinanie))
elif h == "слова, числа, знаки препинания":
    print(random.choice(om)+random.choice(todo_list)+random.choice(om)+random.choice(prepinanie))
elif h == "числа, знаки препинания":
    print(random.choice(todo_list)+random.choice(prepinanie))
if h == "слова, заглавные буквы":
    print(random.choice(om)+random.choice(u_k))