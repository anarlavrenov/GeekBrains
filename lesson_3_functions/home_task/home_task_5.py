user_numbers = input('Введите числа через пробел ')
user_numbers_split = user_numbers.split(' ')

user_list = []

for element in user_numbers_split:
    user_int = int(element)
    user_list.append(user_int)
print(sum(user_list))

while user_numbers != '-':
    user_numbers = input('Введите снова числа через пробел ')
    try:
        if user_numbers == '-':
            break
        user_numbers_split = user_numbers.split(' ')
        for element in user_numbers_split:
            user_int = int(element)
            user_list.append(user_int)
            print(sum(user_list))
    except ValueError:
        break

print('Конец')








