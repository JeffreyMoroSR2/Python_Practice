#Пошук локальних екстремумів у масиві

numbers_list = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
amount = 0
flag = '0'


for i in range(0, len(numbers_list)):
    if i == 0 or numbers_list.index(numbers_list[i]) == len(numbers_list) - 1:
        amount += 1
    elif flag == "0" and numbers_list[i] > numbers_list[i - 1]:
        flag = '1'
    elif flag == '0' and numbers_list[i] < numbers_list[i - 1]:
        flag = '-1'
    elif flag == '1' and numbers_list[i] < numbers_list[i - 1]:
        amount += 1
        flag = '0'
    elif flag == '-1' and numbers_list[i] > numbers_list[i - 1]:
        amount += 1
        flag = '0'

print(amount)


