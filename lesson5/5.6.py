"""
Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и
лабораторных занятий по этому предмету и их количество. Важно, чтобы для
каждого предмета не обязательно были все типы занятий. Сформировать
словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.

"""


def not_digit_but_number(w: str):
    result = ""
    for letter in w:
        if letter.isdigit():
            result += letter
    return result


result_dict = dict()

with open("subjects.txt", "r") as f_operation:
    for line in f_operation:
        line = line.split(" ")
        # print(line)
        res = 0
        for word in line:
            if not_digit_but_number(word) != "":
                res += int(not_digit_but_number(word))
        result_dict.update({line[0][:-1]: res})

print(result_dict)
