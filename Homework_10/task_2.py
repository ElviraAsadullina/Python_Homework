# Возьмите любую из задач с прошлых семинаров.
# Превратите функции в методы класса, а параметры - в свойства.
# Задача должна решаться через вызов методов экземпляра.
import sys


class ATM:
    def __init__(self, balance, operations_count):
        self.balance = balance
        self.operations_count = operations_count

    def print_balance(self):
        print(f'Your balance is {self.balance} c.u.')

    @staticmethod
    def general_processing(func):
        def wrapper(self, amount):
            if amount % 50 == 0:
                func(self, amount)
                self.operations_count += 1
                if self.operations_count % 3 == 0:
                    self.balance += self.balance * 0.03
                if self.balance > 5000000:
                    self.balance -= self.balance * 0.1
                self.print_balance()
            else:
                print('Invalid amount! Amount must be a multiple of 50!')
        return wrapper

    @general_processing
    def top_up(self, amount):
        self.balance += amount

    @general_processing
    def withdraw(self, amount):
        if amount <= self.balance:
            fee = amount * 0.015
            if fee < 30:
                fee = 30
            elif fee > 600:
                fee = 600
            if self.balance - amount - fee > 0:
                self.balance -= amount + fee
            else:
                self.operations_count -= 1
                print('Operation cancelled! Balance can not be less than zero!')
        else:
            print('Insufficient balance!')

    @staticmethod
    def exit():
        print('Have a nice day!')
        sys.exit()

    def run(self):
        while True:
            print('\n\33[7m' + 'MAIN MENU' + '\033[0m\n\n'
                                             '1 - Top up\n'
                                             '2 - Withdraw\n'
                                             '3 - Quit\n')
            choice = input('Choose action: ')
            if choice == "1":
                amount = float(input('Input amount to top up: '))
                self.top_up(amount)
            elif choice == "2":
                amount = float(input('Input amount to withdraw: '))
                self.withdraw(amount)
            elif choice == "3":
                self.exit()
            else:
                print('Invalid choice! Please try again!')


bank_account = ATM(0, 0)
bank_account.run()
