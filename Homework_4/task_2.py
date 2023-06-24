# Напишите функцию для транспонирования матрицы
def transpose_matrix(mtrx):
    return list(zip(*mtrx))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(*transpose_matrix(matrix), sep='\n')
