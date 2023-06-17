from fractions import Fraction

while True:
    string_1, string_2 = [x for x in input('Input spaced fractions (format x/y): ').split()]
    if string_1.split('/')[1] == '0' or string_2.split('/')[1] == '0':
        print('--Fraction denominator must not be zero! Try again!--\n')
    else:
        break

lst_1 = [int(x) for x in string_1.split('/')]
lst_2 = [int(x) for x in string_2.split('/')]

plus = (lst_1[0] * lst_2[1] + lst_2[0] * lst_1[1]) / (lst_1[1] * lst_2[1])
mult = (lst_1[0] * lst_2[0]) / (lst_1[1] * lst_2[1])

print('\nSum of fractions:', plus, '\nOK' if plus == float(Fraction(string_1) + Fraction(string_2))
      else '\nWrong result!')
print('\nProduct of fractions:', mult, '\nOK' if mult == float(Fraction(string_1) * Fraction(string_2))
      else '\nWrong result!')
