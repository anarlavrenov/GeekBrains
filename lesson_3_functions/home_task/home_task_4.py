#Способ 1
# def my_func(x, y):
#     return x**y
# print(my_func(3.4, -2))

#Способ 2


def my_func(x, y):
    n = x
    for number in range(y-1):
        x *= n
    return x
print(my_func(3, 4))







