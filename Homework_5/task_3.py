# Создайте функцию генератор всех чисел Фибоначчи (см. Википедию)
from itertools import islice


def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(*islice(generate_fibonacci(), 15), sep=', ')
