"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

num_1 = float(input("Ведите 1-е число: "))
num_2 = float(input("Ведите 2-е число: "))
num_3 = float(input("Ведите 3-е число: "))


def my_func(var_1, var_2, var_3):
    my_sum = [var_1, var_2, var_3]
    my_sum.remove(min(var_1, var_2, var_3))
    return sum(my_sum)


print(f"Сумаа 2-х наибольших аргументов: {my_func(num_1, num_2, num_3)}")
