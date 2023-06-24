# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
import sys
import logging


def print_balance(balance, wd_fee, cash_back, w_tax):
    print('-' * 56 + f'\nYour balance is {round(balance, 1)} c.u.'
                     f'\nWithdraw fee is {round(wd_fee, 1)}. Cashback is '
                     f'{round(cash_back, 1)}. Wealth tax is {round(w_tax, 1)}')


def print_message(message):
    print(message)


def is_valid_amount(total_amount, amount, choice):
    limit_min = 50
    if amount % limit_min != 0 or choice == '1' and amount > total_amount:
        return False
    return True


def calc_cashback(cash_back, total_amount, ops_count):
    cashback_rate = 3
    if ops_count != 0 and ops_count % cashback_rate == 0:
        cash_back += total_amount / 100 * cashback_rate
    return cash_back


def calc_withdraw_fee(wd_fee, amount, choice):
    wd_rate = 1.5
    min_fee, max_fee = 30, 600
    if choice == '1':
        wd_fee = amount / 100 * wd_rate
        if wd_fee < min_fee:
            wd_fee = min_fee
        elif wd_fee > max_fee:
            wd_fee = max_fee
    return wd_fee


def calc_wealth_tax(w_tax, total_amount):  # налог на богатство рассчитывается из суммы, превышающей 5_000_000
    limit_balance = 5_000_000
    if total_amount > limit_balance:
        w_tax = (total_amount - limit_balance) / 100 * 10
    return w_tax


def go_menu(total_amount, ops_count):
    print('\n\33[7m' + 'MAIN MENU' + '\033[0m\n\n'
                                     '1 - Withdraw\n'
                                     '2 - Top up\n'
                                     '3 - Quit\n')

    choice = input('Choose action: ')
    amount, cash_back, wd_fee, w_tax = 0.0, 0.0, 0.0, 0.0

    match choice:
        case '1' | '2':
            amount = float(input('Input amount: '))
            if is_valid_amount(total_amount, amount, choice):
                if choice == '1':
                    total_amount -= amount
                    msg = 'cashed'
                else:
                    total_amount += amount
                    msg = 'topped up'

                w_tax = calc_wealth_tax(w_tax, total_amount)
                cash_back = calc_cashback(cash_back, total_amount, ops_count)
                wd_fee = calc_withdraw_fee(wd_fee, amount, choice)

                if total_amount + cash_back - wd_fee - w_tax < 0:
                    total_amount += amount - w_tax
                    cash_back, wd_fee = 0.0, 0.0
                    print_message('Operation failed! Total withdraw can not exceed balance!')
                    logging.info(f'Operation failed. Amount exceeds balance')
                else:
                    print_message(f'\nSuccessfully {msg} {amount} c.u.')
                    ops_count += 1
                    logging.info(f'{msg}: {amount}.')
            else:
                print_message('\nOperation failed! Amount must be multiple of 50 and must not exceed balance!.')
                logging.info(f'Operation failed. Wrong amount input')
        case '3':
            print_message('Have a nice day!')
            logging.info(f'Session closed')
            sys.exit()
        case _:
            print_message('Invalid input! Please try again!')
            logging.info(f'Wrong action chosen')

    w_tax = calc_wealth_tax(w_tax, total_amount)
    total_amount += cash_back - wd_fee - w_tax
    print_balance(total_amount, wd_fee, cash_back, w_tax)
    go_menu(total_amount, ops_count)


logging.basicConfig(level=logging.INFO, filename="log_operations.log", format="%(asctime)s %(message)s")
amount_total = 0.0
operations_count = 1  # счетчик количества операций для своевременного начисления кэшбэка
go_menu(amount_total, operations_count)
