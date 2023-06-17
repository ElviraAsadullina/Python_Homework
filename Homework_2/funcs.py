def check_input():
    while True:
        number = input('Input any integer number: ')
        if number.isdecimal():
            return int(number)
        print('--Invalid input! Please try again!--\n')
