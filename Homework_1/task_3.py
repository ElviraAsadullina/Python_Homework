# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код: from random import randint, num = randint(LOWER_LIMIT, UPPER_LIMIT).
from random import randint

num = randint(0, 1000)
tries = 10

while tries > 0:
    my_num = int(input('Введите ваше число: '))
    tries -= 1
    match num:
        case num if num > my_num:
            print('Возьмите число побольше! Осталось попыток:', tries)
        case num if num < my_num:
            print('Возьмите число поменьше! Осталось попыток:', tries)
        case _:
            print('Вы угадали число! Компьютер загадал число', num)
            break
else:
    print(f'Вам не удалось угадать число {num}. Попыток больше не осталось.')
