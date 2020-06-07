"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при
достижении числа 10 завершаем цикл. Во втором также необходимо
предусмотреть условие, при котором повторение элементов списка будет
прекращено.

"""

import itertools


# а) итератор, генерирующий целые числа, начиная с указанного,

def int_generator():
    a = input("Введите число, начинающее цикл ")
    b = input("Введите число, завершающее цикл ")
    a = int(a)
    b = int(b)

    for el in itertools.count(a):
        if el > b:
            break
        else:
            yield el


# б) итератор, повторяющий элементы некоторого списка,
# определенного заранее.

def list_elements_generator(given_list: list):
    list_iter = itertools.cycle(given_list)
    c = next(list_iter)
    i = 0
    while i <= 15:
        yield c
        c = next(list_iter)
        i += 1


origin_list = ["word_1", 5, "word_2", False, None, "word_3"]
for itm in list_elements_generator(origin_list):
    print(itm)

for itm in int_generator():
    print(itm)
