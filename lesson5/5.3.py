"""
Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет
оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.

"""

line_list = []
with open("workers.txt", "r") as f_operation:
    for line in f_operation:
        line_list.append(line)

workers_list = dict()
for itm in line_list:
    words = itm.split(" - ")
    if words[1][len(words[1]) - 1] == "\n":
        workers_list.update({words[0]: int(words[1][:-1])})
    else:
        workers_list.update({words[0]: int(words[1])})

result_sum = 0

for itm in workers_list:
    if workers_list.get(itm) < 20000:
        print(itm)
        result_sum += workers_list.get(itm)
    else:
        result_sum += workers_list.get(itm)

result_sum = result_sum / len(workers_list)

# print(result_sum)
# print(len(workers_list))
