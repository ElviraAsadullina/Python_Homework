# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.
# --------------------------------------------------------------------------------------------
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.
# ----------------------------------------------------------------------------------------------
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения
from random import randint


class Rectangle:
    """
    Class creates an instance of Rectangle that keeps rectangle length and width. If rectangle is a square
    then length == width

    Instance attributes:
        length: int|float  -- rectangle length --
        width: int|float  --rectangle width --

    Methods:
        get_p()  -- returns perimeter of Rectangle --
        get_area()  -- returns area of Rectangle --
        __add__()  --returns Rectangle instance with perimeter = sum of given rectangles perimeters --
        __sub__()  -- returns Rectangle instance with perimeter = subtraction of given rectangles perimeters --
        __ge__()  -- returns result of Rectangles comparison ">=" --
        __gt__()  -- returns result of Rectangles comparison ">" --
        __eq__()  -- returns result of Rectangles comparison "==" --
        __str__()  -- instance representation for user --
        __repr__()  -- instance representation for developer --
    """
    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def get_p(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        new_p = self.get_p() + other.get_p()
        new_length = self.length + other.length
        new_width = new_p / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_p = abs(self.get_p() - other.get_p())
        if new_p == 0:
            return f'Can not create Rectangle as subtraction of perimeters is Zero!'
        new_length = new_p / 100
        new_width = new_p / 2 - new_length
        return Rectangle(new_length, new_width)

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __str__(self):
        return f'Rectangle class instance: {self.__dict__}'

    def __repr__(self):
        return f'Rectangle({self.length, self.width})'


r_1 = Rectangle(4, 5)
print(r_1)
print(repr(r_1))

r_2 = Rectangle(1, 9)
print(r_2)
print(repr(r_2))

print(r_1 == r_2)

r_3 = r_1 + r_2
print(f'{r_1.__dict__} + {r_2.__dict__} = {r_3}')

r_4 = r_1 - r_2
print(f'{r_1.__dict__} - {r_2.__dict__} = {r_4}')
