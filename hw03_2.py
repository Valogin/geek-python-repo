"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user_profile(first_name, last_name, birthday, city, email, phone):
    return print(f"Имя: {first_name} Фамилия: {last_name} Год рождения: {birthday}"
                 f" Город проживания: {city} Email: {email} Телефон: {phone}"
                 )


user_profile(
    last_name = input("Фамилия: "),
    first_name = input("Имя: "),
    birthday = input("Год Рождения: "),
    city = input("Город проживания: "),
    email = input("email: "),
    phone = input("phone: "),
)
