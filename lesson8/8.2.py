"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления
на нуль. Проверьте его работу на данных, вводимых пользователем. При
вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.

"""


class MyZeroDivision(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


a = input("Введите делимое \n")
b = input("Введите делитель \n")

try:
    if int(b) == 0:
        raise MyZeroDivision("Деление на ноль недопустимо")
    c = int(a) / int(b)
    print(c)
except MyZeroDivision as e:
    print(e)
