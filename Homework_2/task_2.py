from fractions import Fraction

while True:
    string_1, string_2 = [x for x in input('Input spaced fractions (format x/y): ').split()]
    if string_1.split('/')[1] == '0' or string_2.split('/')[1] == '0':
        print('--Fraction denominator must not be zero! Try again!--\n')
    else:
        break


def reduce_fraction(x, y):
    m = min(x, y)
    if x % y == 0 or y % x == 0:
        x, y = x / m, y / m
    return f'{int(x)}/{int(y)}'


lst_1 = [int(x) for x in string_1.split('/')]
lst_2 = [int(x) for x in string_2.split('/')]

a = lst_1[0] * lst_2[1] + lst_2[0] * lst_1[1]
b = lst_1[1] * lst_2[1]
plus = a / b

a_1 = lst_1[0] * lst_2[0]
b_1 = lst_1[1] * lst_2[1]
mult = a_1 / b_1

print(f'\nSum of fractions: {reduce_fraction(a, b)}'
      '\nOK' if plus == float(Fraction(string_1) + Fraction(string_2)) else '\nWrong result!')
print(f'\nProduct of fractions: {reduce_fraction(a_1, b_1)}' 
      '\nOK' if mult == float(Fraction(string_1) * Fraction(string_2)) else '\nWrong result!')
