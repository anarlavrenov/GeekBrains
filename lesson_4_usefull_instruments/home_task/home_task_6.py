from itertools import count, cycle


for el in count(3, 2):
    print(el)
    if el == 55:
        break


my_list_str = ['anar', 'sveta']
c = 0

for el in cycle(my_list_str):
    print(el)
    if c > 10:
        break
    c += 1

