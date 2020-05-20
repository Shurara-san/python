"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.

"""
seasons = {"winter": [12, 1, 2], "spring": [3, 4, 5], "summer": [6, 7, 8],
           "autumn": [9, 10, 11]}

m_number = input("Введите номер месяца\n")

for a, b in seasons.items():
    if int(m_number) in b:
        print(a)
        break

seasons_list = ["winter", "spring", "summer", "autumn"]
if int(m_number) < 3 or int(m_number) == 12:
    print(seasons_list[0])
elif 3 <= int(m_number) <= 5:
    print(seasons_list[1])
elif 6 <= int(m_number) <= 8:
    print(seasons_list[2])
else:
     print(seasons_list[3])
