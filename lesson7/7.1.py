"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список
списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода
матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый
элемент первой строки первой матрицы складываем с первым элементом первой
строки второй матрицы и т.д.

"""


class Matrix:
    def __init__(self, *args: list):
        self.itm = list(args)

    def __str__(self):
        result = ""
        for i in self.itm:
            result += str(i) + "\n"
        return result

    def __getitem__(self, item):
        return self.item

    def __add__(self, other):
        # return Matrix(list(map(lambda y: list(map(sum, y)),
        #               map(lambda x: list(zip(*x)), zip(self, other))
        #                        )
        #                    )
        #               )
        result = []
        result1 = []
        i = 0
        k = 0
        while i < len(self.itm):
            while k < len(self.itm[0]):
                if self.itm[i][k]:
                    if other.itm[i][k]:
                        summ = int(self.itm[i][k]) + int(other.itm[i][k])
                    else:
                        summ = int(self.itm[i][k])
                else:
                    summ = int(other.itm[i][k])
                k += 1
                result1.append(summ)
            result.append(result1)
            result1 = []
            i += 1
            k = 0
        return Matrix(result)


# a = Matrix([1, 2, 3, 4], [2, 4, 5, 5], [6, 7, 8, 6])
# b = Matrix([1, 2, 3, 7], [2, 4, 5, 7], [6, 7, 8, 9])
