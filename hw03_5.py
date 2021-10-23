"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def calculate_sum(*nums):
    my_sums = 0
    flag = False
    for num in nums:
        try:
            if num:
                my_sums += float(num)
        except ValueError:
            flag = True
    return my_sums, flag


general_sum = 0

while True:
    numbers_string = input("Введите числа через пробел и/или букву для завершения: ").split(" ")
    my_sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += my_sum
    print(f"сумма {general_sum}")

    if stop_flag:
        break
