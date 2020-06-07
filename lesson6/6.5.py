"""
Реализовать класс Stationery (канцелярская принадлежность). Определить
в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.

"""


class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print("Запуск более яркой отрисовки")


class Pencil(Stationery):

    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print("Запуск менее яркой отрисовки")


class Handle(Stationery):

    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print("Запуск наиболее яркой отрисовки")


stat_1 = Stationery("Скотч")
stat_2 = Pencil("Синий карандаш")
stat_3 = Pen("Красная ручка")
stat_4 = Handle("Зелёный маркер")

stat_1.draw()
stat_2.draw()
stat_3.draw()
stat_4.draw()
