# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
# в пару списков-архивов.
# list-архивы также являются свойствами экземпляр.
# --------------------------------------------------------------------------------------
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.
class Archive:
    """
    Class creates a singleton instance that keeps a pair of values (number and string) that is overwritten
    upon attempt to create a new instance. Pair of previous values is being archived into respective lists
    (list of numbers, list of strings).

    Class attributes:
        number: int|float  -- first value in pair --
        string: str  --second value in pair --

    Instance attributes:
        number: int|float  -- first value in pair --
        string: str  --second value in pair --

    Methods:
        __str__()  -- instance representation for user --
        __repr__()  -- instance representation for developer --
    """

    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_numbers = []
            cls._instance.archive_strings = []
        else:
            cls._instance.archive_numbers.append(cls._instance.number)
            cls._instance.archive_strings.append(cls._instance.string)
        return cls._instance

    def __init__(self, number, string):
        self.number = number
        self.string = string

    def __str__(self):
        return f'Is Archive singleton class instance with attributes: {self.__dict__}'

    def __repr__(self):
        return f'Archive({self.number, self.string})'


ar_1 = Archive(1, 'one')
print(ar_1)
print(repr(ar_1))
# print(ar_1. __dict__)
ar_2 = Archive(2, 'two')
print(ar_2)
print(repr(ar_2))
# print(ar_2. __dict__)
print(ar_1 is ar_2)
ar_3 = Archive(3, 'three')
print(ar_3)
print(repr(ar_3))
print(f'Numbers archive: {ar_1.archive_numbers}')
print(f'Strings archive: {ar_1.archive_strings}')

