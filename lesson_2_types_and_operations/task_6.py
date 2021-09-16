#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]



# goods = []
#
# while True:
#     user_answer = input('Продолжать? y/n ')
#     if user_answer == 'y':
#         my_dict = dict({'название': input('Введите название товара '),
#                         'цена': input('Введите цену товара '),
#                         'количество': input('Введите количество товара '),
#                         'ед.': input('Введите единицу товара ')})
#         goods.append((len(goods)+1, my_dict))
#     elif user_answer == 'n':
#         break
#     else:
#         print('Продолжать? y/n ')
#
# print(goods)

#Аналитика

goods = [
    (1, {'название': 'компьютер', 'цена': '20000', 'количество': '3', 'ед': 'шт'}),
    (2, {'название': 'принтер', 'цена': '5000', 'количество': '2', 'ед': 'шт'}),
    (3, {'название': 'монитор', 'цена': '3000', 'количество': '5', 'ед': 'шт'})
]

my_dict = {}

for element in goods:
    position, info = element #Нужно выучить распаковывание
    for key, value in info.items():
        value_list = my_dict.get(key, [])
        if value not in value_list:
            value_list.append(value)
            my_dict[key] = value_list
print(my_dict)




