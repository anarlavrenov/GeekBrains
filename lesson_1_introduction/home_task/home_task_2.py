seconds_input = int(input('Введите к-во секунд '))

hours = seconds_input // 3600 #Двойное деление - узнать целок к-во, без десятичных
minutes = seconds_input % 3600 // 60 #Процент - узнать остаток секунд, затем оставшиеся секунды перевожу в минуты
seconds = seconds_input % 3600 % 60 #Нахожу остаток секунд
print(hours)
print(minutes)
print(seconds)

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}') #02d определяет к-во символов в строке

