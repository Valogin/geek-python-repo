"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    pass


def division_func(a, b):
    try:
        res = round(a / b, 2)
    except ZeroDivisionError:
        print(f"{a} / {b} -> на ноль делить нельзя!\n")
    else:
        print(f"{a} / {b} = {res} \n")


division_func(1, 2)
division_func(1, 0)
division_func(-1, 3)
division_func(0, 4)
