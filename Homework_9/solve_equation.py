# Напишите следующие функции: нахождение корней квадратного уравнения
from Homework_9.decorators import use_csv_data, write_to_json


@use_csv_data('nums.csv')
@write_to_json('result.json')
def find_equation_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    match d:
        case d if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            return x1, x2
        case d if d == 0:
            x1 = -b / (2 * a)
            return x1
        case _:
            return 'Equation has no roots!'


print(find_equation_roots(-5, 6, 400))
