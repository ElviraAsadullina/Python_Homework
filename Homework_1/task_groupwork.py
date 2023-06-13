# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
from colorama import Fore, Back

START = 2
END_FIRST_MULTIPLIER, END_SECOND_MULTIPLIER = 9, 11
step = 4

print(Back.GREEN + Fore.BLACK + ' ' * 28 + 'ТАБЛИЦА УМНОЖЕНИЯ')

for row in range(START, END_FIRST_MULTIPLIER, step):
    for i in range(START, END_SECOND_MULTIPLIER):
        for j in range(row, row + step):
            print(Back.GREEN + Fore.BLACK + f'{j}  x {i:>2}  =  {i * j:>2}', end=' '*6)
        print()
    print()
