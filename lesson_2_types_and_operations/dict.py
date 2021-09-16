#Словарь - изменяемый тип данных

dict = {'mazda': 10000,
        'nissan': 5000,
        'volvo': 3000
}

#Конвертация строки, введенной пользователем в словарь
input = input('Enter the name of the car and the price')
dict = {input.split()[0] : input.split()[1]}
print(dict)