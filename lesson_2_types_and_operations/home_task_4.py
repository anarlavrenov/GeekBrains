user_str = input('Введите строку ')
user_new_str = user_str.split()

user_list = list(user_new_str)


for ind, el in enumerate(user_list, 1):
    print(ind, el)


