"""
Звездный Python

Оператор * соответствует распаковке последовательности
"""

my_list = [20, 30, 40, 50]

el_1, el_2, el_3, el_4 = my_list
print(el_1, el_2, el_3, el_4)

print(*my_list)  # * передает все элементы my_list в print

*el_1, el_2, el_3 = my_list
print(el_1, el_2, el_3)

el_1, *el_2, el_3 = my_list
print(el_1, el_2, el_3)

el_1, el_2, *el_3 = my_list
print(el_1, el_2, el_3)

el_1, el_2, el_3, *el_4 = my_list
print(el_1, el_2, el_3, el_4)

el_1, el_2, el_3, el_4, *el_5 = my_list
print(el_1, el_2, el_3, el_4, el_5)

my_dict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5}
key_value_pairs = my_dict.items()
print(key_value_pairs)

el_1, *el_2 = key_value_pairs
print(el_1, el_2)

for key, value in my_dict.items():
    print(key, value)

names = ("Иван", "Николай", "Сергей", "Петр", "Саша")
surnames = ("Иванов", "Николаев", "Сергеев", "Петров")

for name, surname in zip(names, surnames):
    print(f"{name} {surname}")


names = ("Иван", "Николай", "Сергей", "Петр", "Саша")
surnames = ("Иванов", "Николаев", "Сергеев", "Петров")


for name, surname in zip(names, surnames):
    print(f'{name} {surname}')
