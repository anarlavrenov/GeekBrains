#Нужен, чтобы не хранить весь пакет данных, а вызывать только часть. Yield - это return, только можно использовать несколько раз
#и хранит только один обьект в себе
import itertools


def gen():
    x = 42
    yield x
    x += 1
    yield x
    x += 1
    yield x

g = gen()
print(g)
print(next(g)) # - Выведет первый х
print(next(g))
print(next(g))

for i in gen():
    print(i)  #- Выведет все элементы (иксы). Перепрыгнуть элементы нельзя


#Генератор списков
#выражение, for j in итерируемый обьект if условие. Обвалакиваю всё это в переменную.
#В списке выведет всё сразу, в круглых скобках (генератор) - по одному будет. Через next()

#Map() - не рекомендуется (тоже самое по смыслу, что генератор)
#filter() - не рекомендуется (тоже самое по смыслу, что генератор)


# темы урока
#
# yield
# генератор списков
# import
# sys argv
# модули random, fanctools (reduce (5+3)+3)+3, partial - cохраняет параметры, чтобы потом в принте при вызову функции
# не указывать снова и снова)
#
# модуль itertools.count (0, 2) - от нуля  с шагом два до бесконечности. Itertools - module, count - method
# itertools.cycle - бесконечный перебор по кругу (списка, например
# itertools.chain(range(2), range(4,8)) - сначала один рейндж пошел, потом второй пошел и так далее (по одному шагу) на аждый рейндж)
# module time. time.sleep(5) - каждые пять секунд будет вывод, а не сразу всё
