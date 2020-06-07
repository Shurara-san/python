"""
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с
декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной
структуры на реальных данных.

"""


class Date:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_format(cls, date):
        day = int(date.split("-")[0])
        month = int(date.split("-")[1])
        year = int(date.split("-")[2])
        return [day, month, year]

    @staticmethod
    def date_validation(day: int, month: int, year: int):
        if 12 < month or 31 < day:
            print("Введена невозможная дата")
            return False
        elif (month // 2 != 0 or month == 2) and day > 28:
            if month == 2:
                if day > 29 and (year // 400 == 0 or (year // 4 == 0 and year // 100 != 0)):
                    print("В этом году в феврале 29 дней, но не больше")
                    return False
                elif day > 28 and (year // 400 != 0 or (year // 4 != 0 and year // 100 == 0)):
                    print("В этом году в феврале 28 дней")
                    return False
            print("В заданом месяце 30 дней")
            return False
        else:
            return True


# m = "30-02-3"
# d = Date(m)
# print(d.date_format(m))
# print(d.date_validation(d.date_format(m)[0], d.date_format(m)[1],
#                          d.date_format(m)[2]))
