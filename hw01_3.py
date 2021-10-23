"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
"""

number = int(input("Введите число: "))

number = str(number)
nn = int(number + number)
nnn = int(number + number + number)
summa = int(number) + nn + nnn

print(summa)
