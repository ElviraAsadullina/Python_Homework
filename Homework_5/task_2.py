# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем
# словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как
# ставка умноженная на процент премии.
def get_dict(lst_1, lst_2, lst_3):
    return ({n: s / 100 * float(b[:-1])} for n, s, b in zip(lst_1, lst_2, lst_3))


names = ['Ruslan', 'Pavel', 'Dmitry']
rate = [100_000, 110_000, 120_000]
bonus = ['10.25%', '12.5%', '20.0%']

print(*get_dict(names, rate, bonus))
