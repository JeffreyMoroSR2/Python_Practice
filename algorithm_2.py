#Пошук локальних екстремумів у масиві

numbers_list = [1, 2, 3, 0, -1, 4, 5]
new_arr = []

for i in range(0, len(numbers_list)):
    if numbers_list.index(numbers_list[i]) == 0 or numbers_list.index(numbers_list[i]) == len(numbers_list) - 1:
        new_arr.append(numbers_list[i])
    elif numbers_list[i] > numbers_list[i - 1] and numbers_list[i] > numbers_list[i + 1]:
        new_arr.append(numbers_list[i])
    elif numbers_list[i] < numbers_list[i - 1] and numbers_list[i] < numbers_list[i + 1]:
        new_arr.append(numbers_list[i])

print(new_arr)
