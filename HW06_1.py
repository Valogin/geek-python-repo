"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = ""

    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print("Светофор работает")
        i = 0
        while i < len(self.__color):
            print(f"Горит {self.__color[i]}")

            if i == 0:
                start_time = time.time()
                time.sleep(7)
                print(f"Время работы {round(time.time()-start_time)} секунд")
            elif i == 1:
                start_time = time.time()
                time.sleep(5)
                print(f"Время работы {round(time.time()-start_time)} секунд")
            elif i == 2:
                start_time = time.time()
                time.sleep(4)
                print(f"Время работы {round(time.time()-start_time)} секунд")

            i += 1


t = TrafficLight()
t.running()
