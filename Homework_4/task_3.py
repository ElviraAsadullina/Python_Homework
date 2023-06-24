# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
from collections.abc import Iterable


def get_dict(**kwargs):
    my_dict = {str(v)[1:-1] if isinstance(v, Iterable) else v: k for k, v in kwargs.items()}
    return my_dict


print(get_dict(perfect=[5, '5+'], good=4, bad=3, awful=[2, 1]))
