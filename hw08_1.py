"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def from_string(cls, day_month_year):

        day, month, year = map(int, day_month_year.split('-'))
        return day, month, year

    @staticmethod
    def is_date_valid(day_month_year):

        day, month, year = map(int, day_month_year.split('-'))

        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 2050:
            return f"{day} {month} {year}"
        else:
            print("Недопустимое значение даты")


date = '12-10-2000'
print(date)
print(Date.from_string(date))
print(Date.is_date_valid(date))
