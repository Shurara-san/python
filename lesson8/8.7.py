"""
Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.

"""

class ComplexNumber:
    def __init__(self, a, b):
        self.real = int(a)
        self.complex = int(b)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.complex + other.complex)

    def __mul__(self, other):
        real_part = self.real * other.real - self.complex * other.complex
        complex_part = self.real * other.complex + self.complex * other.real
        return ComplexNumber(real_part, complex_part)

    def __str__(self):
        if self.complex > 0:
            if self.complex == 1:
                return str(self.real) + " " + str(self.complex) + "i"
            else:
                return str(self.real) + " + " + str(self.complex) + "i"
        else:
            if self.complex == -1:
                return str(self.real) + " - " + "i"
            else:
                return str(self.real) + " - " + str(-self.complex) + "i"


a = ComplexNumber(2, 3)
b = ComplexNumber(-1, 1)
c = a * b
d = a + b
print(c)
print(d)
