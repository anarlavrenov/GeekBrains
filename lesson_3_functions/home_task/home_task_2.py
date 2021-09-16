def info(name, surname, age, city, email, phone):
    value_1 = f'Тебя завут {name} {surname},'
    value_2 = f'Тебе {age} года,'
    value_3 = f'Ты живешь в городе {city},'
    value_4 = f'Твой email - это {email},'
    value_5 = f'твой телефон: {phone},'
    return value_1, value_2, value_3, value_4, value_5

my_value_1, my_value_2, my_value_3, my_value_4, my_value_5 = info(name='Анар', surname='Лавренов', age='24', city='Киев', email='anarstanislavlavrenov', phone='0681935580')
print(my_value_1, my_value_2, my_value_3, my_value_4, my_value_5)