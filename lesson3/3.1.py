"""

Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.

"""


def my_div():
    a = input("Введите делимое\n")
    b = input("Введите делитель\n")
    a = int(a)
    b = int(b)
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Деление на ноль!")
        result = 0
        return result
