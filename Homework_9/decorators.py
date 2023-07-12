# Напишите следующие функции:
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from functools import wraps


def use_csv_data(csv_file):
    def deco(func):
        res = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(csv_file, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    args = map(int, row)
                    res.append(func(*args, **kwargs))
            return res
        return wrapper
    return deco


def write_to_json(json_file):
    def deco(func):
        j = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            my_dict = {'args': args,
                       'result': res}
            j.append(my_dict)
            with open(json_file, 'w', encoding='utf-8') as f1:
                json.dump(j, f1, indent=2)
            return my_dict
        return wrapper
    return deco
