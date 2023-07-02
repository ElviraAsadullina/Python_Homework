# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок.
import time
from pack_hw6 import check_ranking as cr

queens_count = 8
current_ranking = [0 for x in range(queens_count)]
combinations = cr.generate_ranking(0, queens_count, current_ranking)

print(f'{len(combinations)} rankings found: ')
time.sleep(1)
print(*combinations, sep='\n')

# Для рандомного вывода 4-х успешных расстановок:
# for c in sample(combinations, 4):
#     print(c)
