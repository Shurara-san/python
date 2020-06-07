"""
4.Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать
параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы,
отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм
валидации вводимых пользователем данных. Например, для указания
количества принтеров, отправленных на склад, нельзя использовать
строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Warehouse:

    def __init__(self, name, quantity, __company_branch):
        self.name = []
        self.name.append(name)
        self.quantity = []
        self.quantity.append(quantity)
        self.__company_branch = []
        self.__company_branch.append(__company_branch)

    def __str__(self):
        result = ""
        i = 0
        while i < len(self.name):
            result += "Количество объектов типа" '"' + str(self.name[i]) + \
               '"' + " равно " + str(self.quantity[i]) + '\n'
            i += 1
        return result

    def item_adding(self, param_1, param_2, param_3):
        self.name.append(param_1)
        self.quantity.append(param_2)
        self.__company_branch = param_3

    def item_transfer(self, new_branch):
        i = self.name.index(self.name)
        self.__company_branch[i] = new_branch



class OfficeEquipment():
    def __init__(self, type, quantity):
        self[type] = quantity


class Printer(OfficeEquipment):
    def __init__(self, type, quantity, color):
        super().__init__(type, quantity)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, type, quantity, worth):
        super().__init__(type, quantity)
        self.color = worth


class Xerox(OfficeEquipment):
    def __init__(self, type, quantity, quality):
        super().__init__(type, quantity)
        self.quality = quality

class IsThisDigit(Exception):
    def __init__(self, txt):
        IsThisDigit.txt = txt


# try:
#     s = input("Введите элементы \n")
#     a, b, c, d = s.split(" ")
#     if not b.isdigit():
#         raise IsThisDigit("Введённый элемент не является числом")
#         new_printer = Printer(a, b, c, d)
# except IsThisDigit as e:
#     print(e)


