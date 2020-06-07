"""
Создать (программно) текстовый файл, записать в него программно набор
чисел, разделенных пробелами. Программа должна подсчитывать сумму
чисел в файле и выводить ее на экран.

"""
import random

with open("numbers.txt", 'w') as f_1:
    n_1 = random.randrange(5, 15)
    i = 0
    while i < n_1:
        f_1.write(str(random.randint(0, 150)) + " ")
        i += 1

n_1 = 0

with open("numbers.txt", 'r') as f_1:
    i = f_1.read()
    print(i)
    i = i.split(" ")
    for itm in i[:-1]:
        n_1 += int(itm)

print(n_1)
