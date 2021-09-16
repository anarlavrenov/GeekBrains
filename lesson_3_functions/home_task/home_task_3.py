def my_func(number_1, number_2, number_3):
    if number_1 > number_2 and number_2 > number_3:
        return number_1 + number_2
    elif number_2 > number_1 and number_1 > number_3:
        return number_2 + number_1
    elif number_3 > number_1 and number_1 > number_2:
        return number_3 + number_1
    elif number_3 > number_2 and number_2 > number_1:
        return number_3 + number_2
    elif number_1 > number_2 and number_2 < number_3:
        return number_1 + number_3
    elif number_3 > number_1 and number_2 > number_3:
        return number_2 + number_3
    else:
        return ('Нельзя вводить одинаковые элементы')

print(my_func(6, 10, 13))
