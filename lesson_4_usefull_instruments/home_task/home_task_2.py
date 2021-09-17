numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 40, 200]

result = []

def calc():
    for ind, elem in enumerate(numbers):
        if numbers[ind] > numbers[ind - 1]:
            result.append(elem)
    result.pop(0)
    return result

print(calc())

