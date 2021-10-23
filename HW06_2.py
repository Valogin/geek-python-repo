"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length: int
    _width: int

    def __init__(self, length, width, roadbed=25, thickness=5):
        self._length = length
        self._width = width
        self.roadbed = roadbed
        self.thickness = thickness

    def asphalt_mass(self):
        print(
            f"Масса асфальта,""\n""необходимого для покрытия всего дорожного полотна"
            f" {round((self._length * self._width * self.roadbed * self.thickness) / 1000)} т."
            )


result = Road(20, 5000)
result.asphalt_mass()
