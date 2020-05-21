"""

Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
новый элемент с тем же значением должен разместиться после них.

"""

my_list = [78, 56, 56, 34, 18, 10, 5, 4, 3, 2, 1]
n = 0
number = int(input("Введите число\n"))
if number in my_list:
    pos = my_list.index(number) + my_list.count(number)
    my_list.insert(pos, number)
else:
    for i in my_list:
        if i < number:
            my_list.insert(my_list.index(i), number)
            n = 1
            break
    if n == 0:
        my_list.append(number)

print(my_list)
