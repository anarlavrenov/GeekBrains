def calc(first_number, second_number):
    return first_number / second_number

user_number_1 = int(input('Введите первое число '))
user_number_2 = int(input('Введите второе число '))

try:
    print(calc(user_number_1, user_number_2))
except ZeroDivisionError:
    print('Деление на ноль')

