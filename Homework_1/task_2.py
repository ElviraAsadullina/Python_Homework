# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
def check_input():
    while True:
        number = input('Введите целое число от 0 до 100 000 для проверки: ')
        if number.isdecimal() and 0 <= (res := int(number)) <= 100000:
            return res
        print('--Введено неверное значение! Попробуйте еще раз!--\n')


EXCEPTION_1, EXCEPTION_2 = 0, 1
START = 2
BORDER_PRIME = 1

num = check_input()
a = [i for i in range(START, num + 1) if (num / i).is_integer()]
print('Простое' if len(a) == BORDER_PRIME else 'Ни простое, ни составное' if num in [EXCEPTION_1, EXCEPTION_2]
      else 'Составное')
