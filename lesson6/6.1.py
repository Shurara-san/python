"""
Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый. Продолжительность первого состояния (красный) составляет
7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше
усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его
нарушении выводить соответствующее сообщение и завершать скрипт.


Пусть продолжительность третьего состочния = 5

"""
import time


class TrafficLight:
    __color = "red"
    __count = 0

    def running(self):
        if TrafficLight.__count == 0:
            TrafficLight.__count = time.time()
        else:
            if 9 > abs(int(time.time()) - int(TrafficLight.__count)) >= 7:
                TrafficLight.__color = "yellow"
            elif 14 > abs(int(time.time()) - int(TrafficLight.__count)) >= 9:
                TrafficLight.__color = "green"
            elif abs(int(time.time()) - int(TrafficLight.__count)) > 14:
                TrafficLight.__color = "red"
                TrafficLight.__count = time.time() + (int(time.time()) - int(TrafficLight.__count))

        # print("цвет:", TrafficLight.__color, "прошло секунд:", abs(int(time.time()) - int(TrafficLight.__count)),
        # "\n")

# start_time = time.time()
# lighter1 = TrafficLight()
# lighter1.running()
#
# while time.time() - start_time < 25:
#     lighter1.running()
