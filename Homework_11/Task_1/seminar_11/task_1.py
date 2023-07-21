# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
from time import time, strftime, gmtime


class MyString(str):
    """
    Class creates an instance that inherits "str" Class scope plus keeps two additional attributes -
    name and time of creation.

    Attributes:
        value: str  -- value of instance itself --
        name: str  -- name of instance --
        init_time: str  -- time of instance creation, format "hh:mm:ss" --

    Methods:
        __str__()  -- instance representation for user --
        __repr__()  -- instance representation for developer --
    """

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.init_time = strftime('%H:%M:%S', gmtime(time()))
        return instance

    def __str__(self):
        return str({'value': self} | self.__dict__)

    def __repr__(self):
        return f'MyString({self.name, self.init_time})'


my_line = MyString('How much is the fish', 'H.P. Baxxter')
print(my_line)
print(repr(my_line))

