"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.

"""

# def translator(word):
#     if

translator = {"One": "Один", "Two": "Два", "Three": "Три",
              "Four": "Четыре"}

f_1 = open("result_txt.txt", "w")
with open("text.txt", "r") as f_2:
    for line in f_2:
        line = line.split(" ")
        line[0] = translator.get(line[0])
        f_1.write(line[0] + " " + line[1] + " " + line[2])
f_1.close()


