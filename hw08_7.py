"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyComplex:
    
    def __init__(self, a, b):
        self.a = complex(a)
        self.b = complex(b)
    
    def __add__(self, other):
        return self.a+self.b
    
    def __mul__(self, other):
        return self.a * self.b


z1 = 1-1j
z2 = 3+6j
rez_z = MyComplex(z1, z2)
print(f"{z1} + {z2} =", rez_z.__add__(rez_z))
print(f"{z1} * {z2} =", rez_z.__mul__(rez_z))
