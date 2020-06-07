"""
Создайте собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу исключения
на реальном примере. Необходимо запрашивать у пользователя данные и
заполнять список. Класс-исключение должен контролировать типы данных
элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются
бесконечно, пока пользователь сам не остановит работу скрипта, введя,
например, команду “stop”. При этом скрипт завершается, сформированный
список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить
только числа и строки. При вводе пользователем очередного элемента
необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить
пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.

"""

class IsThisDigit(Exception):
    def __init__(self, txt):
        IsThisDigit.txt = txt


a = ""
result = []
print("Для выхода введите stop")
while a != "stop":
    try:
        a = input("Введите элемент \n")
        if not a.isdigit():
            raise IsThisDigit("Введённый элемент не является числом")
        result.append(int(a))
    except IsThisDigit as e:
        print(e)

print("Список собран:\n")
print(result)
