# Напишите следующие функции:
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
import csv
from random import randint


def gen_csv(f_name, rows_count, nums_count, rand_start, rand_end):
    with open(f_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['number 1', 'number 2', 'number 3'])
        for _ in range(rows_count):
            row = [randint(rand_start, rand_end) for _ in range(nums_count)]
            writer.writerow(row)


gen_csv('nums.csv', 100, 3, 1, 100)
