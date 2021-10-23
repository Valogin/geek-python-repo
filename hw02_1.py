"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
my_int = 1
my_float = 1.2
my_str = "Hello world"
my_bool = True
my_bytes = b'text'
my_list = [2, 'text', 456, 45.3, None]
my_tuple = (1, 2, 3, 4, 5)
my_dict = {'title': 'Samsung Galaxy', 'price': 20000}

result_list = [my_int, my_float, my_str, my_bool, my_bytes, my_list, my_tuple, my_dict]
for i in result_list:
    print(f'{i} is {type(i)},')
