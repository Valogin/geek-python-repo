"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

my_tuple = tuple([random.randint(0, 5) for i in range(10)])
print(my_tuple)

with open("hw05_5_data.txt", "w", encoding = "utf-8") as f_obj:
    print(*my_tuple, file = f_obj)

with open("hw05_5_data.txt", "r", encoding = "utf-8") as f_obj_2:

    result = sum(map(int, f_obj_2.read().split()))
    print(f"Сумма чисел в файле: {result}")
