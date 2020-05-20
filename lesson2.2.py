"""

2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""
first_list = input("Введите данные через запятую\n")
first_list = first_list.split(',')
i = 0
if len(first_list) % 2:
    while i <= len(first_list) - 3:
        tmp = first_list[i]
        first_list[i] = first_list[i+1]
        first_list[i+1] = tmp
        i += 2
else:
    while i <= len(first_list) - 1:
        tmp = first_list[i]
        first_list[i] = first_list[i+1]
        first_list[i+1] = tmp
        i += 2

print("Изменённый список имеет следующий вид:", first_list[:])
