from functools import reduce


my_list = [number for number in range(100, 1001) if number % 2 == 0]

def my_func(el_1, el_2):
    return el_1 + el_2

print(reduce(my_func, (my_list)))


