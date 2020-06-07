"""
Реализовать проект расчета суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая может
иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для
пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить
работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы для
основных классов проекта, проверить на практике работу декоратора
@property.

"""

from abc import ABC, abstractmethod


class Clothes:
    @property
    @abstractmethod
    def consumption(self) -> float:
        pass

    def total_consumption(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def consumption(self) -> float:
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self) -> float:
        return self.height * 2 + 0.3


# a = Coat(5)
# b = Suit(4)
# print(a.consumption)
# print(b.consumption)
# print(a.total_consumption(b))
