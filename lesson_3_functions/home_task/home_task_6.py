# def func(text):
#     my_str = str(text)
#     return my_str.capitalize()
# print(func('car'))

#
result = []

def func(text):
    my_str = str(text)
    my_str_split = my_str.split(' ')
    for element in my_str_split:
        result.append(element.capitalize())
    return result


print(func('text jim hello'))




