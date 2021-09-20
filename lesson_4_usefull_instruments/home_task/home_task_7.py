import math
from itertools import count

def fact(n):
    for i in count(1):
        yield math.factorial(i)
        if i == n:
            break

for el in fact(5):
    print(el)












