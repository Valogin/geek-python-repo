"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("hw05_2_data.txt", "r") as f_obj:
    a = sum(1 for line in f_obj)
    print(f"В файле {f_obj.name} {a} строки.")

with open("hw05_2_data.txt", "r") as my_f:
    for b, line in enumerate(my_f):
        if len(line.split(' ')) == 1:
            print(f"В строке {b + 1} - {len(line.split(' '))} слово")
        elif 1 < len(line.split(' ')) < 5:
            print(f"В строке {b + 1} - {len(line.split(' '))} слова")
        elif len(line.split(' ')) >= 5:
            print(f"В строке {b + 1} - {len(line.split(' '))} слов")
