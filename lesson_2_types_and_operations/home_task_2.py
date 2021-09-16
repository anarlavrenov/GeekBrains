user_input = (input('Введите числа через проблел '))
user_input = user_input.split()
print(user_input)

for index in range(0, len(user_input), 2):
    user_input[index], user_input[index+1] = user_input[index+1], user_input[index]
print(user_input)


