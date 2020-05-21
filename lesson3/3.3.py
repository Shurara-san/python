"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.

"""


def my_func(n1, n2, n3):
    if (n1 <= n2) and (n1 <= n3):
        result = n2 + n3
    elif (n2 <= n1) and (n2 <= n3):
        result = n1 + n3
    else:
        result = n1 + n2
    return result




