#remove()- удаляет элемент списка (по названию элемента)
#pop() - удаляет элемент списка (по индексу)
#extend(list_name) - добавляет в текущий список другой (в конец)
#insert() - добавляет в списко элемент на нужную позицию (сначала указываю индекс, потом значение)
#index() - показывает индекс элемента в списке (в скобках указываю значение элемента)
#count() - считает к-во повторяющегося элемента (в скобках указываю значение элемента)
#sort() - сортирует список по возростанию
#reverse() - выводит список элементов в обратном порядке
#len() - считает к-во элементов списка
#copy() - создает копию списка в новую переменную. Пример использования: list_copy = list.copy()
#clear() - удаляет список полностю. Если вызвать список после этого действия, то вернется пустой список
#enumerate - показывает индекс и значение каждого элемента списка в виде кортежей. Пример использования:
                                                                    #enumerate(my_list)
#max() - показывает наибольшее число списка
#min() - показывает наименшее число списка
#list[2] = 'b' - заменить указанный элемент списка (по индексу) на желаемый новый элемент
#list[2] = [1, 2, 3, 4, 5] - заменить указанный элемент списка (по индексу) на список
#list[3:5] - вызвать срез елементов списка. Левая граница будет включена, а правая - нет, то есть выведется 2 елемента
#list[3:] - срез от индекса элемента и до конца списка
#list[2:7:2] - вывести срез элементов с указанием шага (третий аргумент)
#list[-1] - получить последний элемент списка