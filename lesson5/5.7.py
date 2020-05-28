"""
Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а
также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила
убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.

"""
import json

firms_list = []
firms_profits = {}
average_profit = {}
a_p = 0
i = 0
with open("firms.txt", "r") as f_1:
    for line in f_1:
        line = line.split(" ")
        if int(line[2]) - int(line[3]) >= 0:
            firms_profits.update({line[0]: int(line[2]) - int(line[3])})
            a_p += int(line[2]) - int(line[3])
            i += 1
        else:
            firms_profits.update({line[0]: -int(line[2]) + int(line[3])})
    # for key in firms_profits:
    #     if firms_profits.get(key) > 0:
    #         a_p += firms_profits.get(key)
    #         i += 1
    a_p = a_p / i
    average_profit.update({"average_profit": a_p})
firms_list.append(firms_profits)
firms_list.append(average_profit)
with open("firms_result.json", "w") as f_2:
    json.dump(firms_list, f_2)
