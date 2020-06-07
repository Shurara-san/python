"""
Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.

"""

f_1 = open("result_file.txt", 'w')
user_str = input("Введите строку. Для завершения, введите пустую строку\n")
f_1.write(user_str + "\n")
f_1.close()
f_1 = open("result_file.txt", 'a')
user_str = input("Введите строку\n")
while user_str != "":
    # запись в файл
    f_1.write(user_str + "\n")
    user_str = input("Введите строку\n")
f_1.close()

# with open("result_file.txt") as f_1:
#     for line in f_1:
#         print(line)
