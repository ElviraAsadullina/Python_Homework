# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
from os.path import splitext, basename, dirname


def split_path(txt):
    return dirname(txt), splitext(basename(txt))[0], splitext(txt)[1][1:]


absolute_path = 'C:/Users/Elvira/Python_Homework/task_1.py'
print(split_path(absolute_path))
