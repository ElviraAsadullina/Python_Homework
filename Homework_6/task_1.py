# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий
# задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг
# друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложью
from random import sample
from pack_hw6.check_ranking import is_harmless_pair_1

queens_count = 8
board_size = 8
current_ranking = sample([(x, y) for x in range(board_size) for y in range(board_size)], queens_count)
print(current_ranking)
print(is_harmless_pair_1(current_ranking))
