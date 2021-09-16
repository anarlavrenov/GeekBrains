my_list = [1, 4, 3, 7, 6]

user_input = (int(input('Введите число ')))
my_list.append(user_input)
my_list_added = my_list.copy()
my_list_added.sort()
result = my_list_added.copy()
result.reverse()
print(result)














