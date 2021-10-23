"""
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""
import random


class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police is False:
            print(f"{self.color} {self.name} начал движение")
        else:
            print(f"Полицейский {self.color} {self.name} начал движение")

    def stop(self):
        if self.is_police is False:
            print("доехал до места назначения. :)\n")
        else:
            print("остановил нарушителя. :)\n")

    def turn(self):
        direction = ["в лево,", "в право,", "вперед,", "назад,"]
        a = random.choice(direction)
        b = random.choice(direction)
        c = random.choice(direction)
        d = random.choice(direction)
        print(f"маневрируя {a} {b} {c} {d}")

    def show_speed(self):
        print(f"на скорости {self.speed} км/ч ")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"на скорости {self.speed} км/ч ")
            self.speed = self.speed-60

            print(f"превышая доаустимую скорость на {self.speed} км/ч ")
        else:
            print(f"на скорости {self.speed} км/ч ")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"на скорости {self.speed} км/ч ")
            self.speed = self.speed-40

            print(f"превышая доаустимую скорость на {self.speed} км/ч ")
        else:
            print(f"на скорости {self.speed} км/ч ")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


tc = TownCar(130, "Синий", "Ford focus")
sc = SportCar(230, "Крсный", "Ford mustang")
wc = WorkCar(50, "Серебристый", "Ford ка")
pc = PoliceCar(10, "Черно-белфй", "Ford explorer", True)

tc.go()
tc.show_speed()
tc.turn()
tc.stop()

sc.go()
sc.show_speed()
sc.turn()
sc.stop()

wc.go()
wc.show_speed()
wc.turn()
wc.stop()

pc.go()
pc.show_speed()
pc.turn()
pc.stop()
