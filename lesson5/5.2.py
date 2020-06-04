"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""

line_list = []
with open("some_text.txt", "r") as f_operation:
    for line in f_operation:
        line_list.append(line)

string_number = len(line_list)
word_number = []
for itm in line_list:
    words = itm.split(" ")
    word_number.append(len(words))

# print("количество строк", string_number)
# i = 0
# for itm in word_number:
#     i += 1
#     print("Количество слов в ", i, " строке:", itm)
