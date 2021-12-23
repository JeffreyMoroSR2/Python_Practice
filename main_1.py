#Підрахунок к-сті символів у рядку

while True:
    flag = input("Введіть 1 для початку роботи, 2 - для виходу з програми\n")
    if flag == '1':
        string_line = input("Введіть текст (рахуються всі символи за виключенням цифр)\n")
        string_line = string_line.lower()

        my_dict = {}

        for i in string_line:
            if i.isnumeric():
                continue
            elif i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        if len(my_dict) == 0:
            print("У рядку відсутні необхідні символи")
        else:
            print(my_dict)

    elif flag == '2':
        break
    else:
        print("Не вірно введені дані\n")
        continue


