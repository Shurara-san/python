"""
Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go,
stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для
классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Выполните вызов методов и
также покажите результат.

"""


class Car:

    def __init__(self, speed: float, color: str, name: str,
                 is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print("Скорость машины:", self.speed)

    def go(self):
        print(self.name, "поехала")

    def stop(self):
        print(self.name, "остановилась")

    def turn(self, direction: str):
        print(self.name, "повернула", direction)


class TownCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена (ограничение: 60 км/ч): ", self.speed)
        else:
            print("Скорость машины:", self.speed)


class SportCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WorkCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена (ограничение: 40 км/ч): ", self.speed)
        else:
            print("Скорость машины:", self.speed)


class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


car1 = TownCar(70, "red", "Toyota", False)
car2 = SportCar(90, "yellow", "Pagani", False)
car3 = WorkCar(50, "grey", "Ford", False)
car4 = PoliceCar(100, "blue", "Bugatti", True)

print(car1.speed)
print(car2.color)
print(car3.name)
print(car4.is_police)

car1.show_speed()
car2.show_speed()
car3.go()
car2.stop()
car4.turn("налево")




