"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

while True:
    month_num = input(" Введите месяц в виде целого числа от 1 до 12: ")
    if month_num.isdigit():
        month_num = int(month_num)
        break
    
    print('ошибка ввода, это не число')

time_year_list = ["зима", "весна", "лето", "осень"]
time_year_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}

if month_num == 1 or month_num == 12 or month_num == 2:
    print(f"{month_num}-й месяц в списке это {time_year_dict.get(1)}")
    print(f"{month_num}-й месяц в слваре это {time_year_list[0]}")
elif month_num == 3 or month_num == 4 or month_num == 5:
    print(f"{month_num}-й месяц в списке это {time_year_dict.get(2)}")
    print(f"{month_num}-й месяц в слваре это {time_year_list[1]}")
elif month_num == 6 or month_num == 7 or month_num == 8:
    print(f"{month_num}-й месяц в списке это {time_year_dict.get(3)}")
    print(f"{month_num}-й месяц в слваре это {time_year_list[2]}")
elif month_num == 9 or month_num == 10 or month_num == 11:
    print(f"{month_num}-й месяц в списке это {time_year_dict.get(4)}")
    print(f"{month_num}-й месяц в слваре это {time_year_list[3]}")
else:
    print("Это не то число")
