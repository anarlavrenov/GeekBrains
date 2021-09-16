# try:
#     user_number = int(input('Введите число от 1 до 12 '))
# except ValueError:
#     print('Введите число')
#
# winter = [12, 1, 2]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10 ,11]
#
# if user_number in winter:
#     print('winter')
# elif user_number in spring:
#     print('spring')
# elif user_number in summer:
#     print('summer')
# elif user_number in autumn:
#     print('autumn')


user_number = int(input('Введите число от 1 до 12 '))
my_dict = {}

my_dict = my_dict.fromkeys([12, 1, 2], 'winter')
my_dict.update(my_dict.fromkeys([3, 4, 5], 'spring'))
my_dict.update(my_dict.fromkeys([6, 7, 8], 'summer'))
my_dict.update(my_dict.fromkeys([9, 10, 11], 'autumn'))

print(my_dict.get(user_number))