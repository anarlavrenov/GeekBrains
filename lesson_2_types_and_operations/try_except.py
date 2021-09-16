a  = 500
b  = 0

#Пример 1
# try:
#     a / b
# except ZeroDivisionError as e:
#     print('Деление на ноль', e)
# else:
#     print(a/b)
#

#Пример 2
# my_dict = {'anar': 24, 'sveta': 22}
#
# try:
#     print(my_dict['vlada'])
# except Exception as e:
#     print('Нет такого ключа', type(e))

#Пример 3
try:
    user_input = int(input('Введите цифровое значение '))
except ValueError as e:
    print('Введите числовое значение', type(e))
else:
    print(user_input)


