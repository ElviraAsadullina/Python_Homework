# Создайте класс Матрица. Добавьте методы для:
# вывода на печать, проверку на равенство, сложения, *умножения матриц.
from pprint import pformat as pf


class Matrix:
    """
    Class creates a Matrix and allows to compare, add and multiply Matrices

    Attributes:
        content: two-dimensional array  -- keeps values of Matrix --
        rows: int  -- rows count --
        cols: int  -- columns count --

    Methods:
        __eq__()  -- compares Matrices by equality/non-equality --
        __add__()  -- processes Matrices addition --
        __mul__()  -- processes Matrices multiplication --
        __str__()  -- instance representation for user --
        __repr__()  -- instance representation for developer --
    """
    def __init__(self, content):
        self.content = content
        self.rows = len(self.content)
        self.cols = len(self.content[0])

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.content[i][j] != other.content[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrices must be of the same size to add!')
        result = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.content[i][j] + other.content[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError('First matrix columns number must be equal to second matrix rows number!')
        result = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] = self.content[i][k] * other.content[k][j]
        return Matrix(result)

    def __str__(self):
        return pf(f'Matrix{self.content}')

    def __repr__(self):
        return f'Matrix(content = {self.content}, rows = {self.rows}, columns = {self.cols})'


m_1 = Matrix([[2, 3, 4], [1, 2, 3]])
print(repr(m_1))

m_2 = Matrix([[1, 2, 3], [2, 2, 2]])
print(repr(m_2))

m_3 = Matrix([[1, 2, 3], [2, 2, 2], [1, 2, 3]])
print(repr(m_3))

print(f'\n{m_1} equals to {m_2} = {m_1 == m_2}\n')

m_4 = m_1 + m_2
print(f'{m_1} + {m_2} = {m_4}\n')


m_5 = m_1 * m_3
print(f'{m_1} * {m_3} = {m_5}\n')
