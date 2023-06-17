from Homework_2.funcs import check_input

num = check_input()
num_hex = f'{num:x}'
print('\nHexadecimal performance :', num_hex, '\nOK' if num_hex == hex(num)[2:] else '\nFail to convert!')
