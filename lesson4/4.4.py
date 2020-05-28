"""
Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000 (включая
границы). Необходимо получить результат вычисления произведения всех
элементов списка.
Подсказка: использовать функцию reduce().

"""

import functools


def my_multiplication(a: float, b: float):
    return a * b


my_list = list(range(100, 1000, 2))

result = functools.reduce(my_multiplication, my_list)

print(result)