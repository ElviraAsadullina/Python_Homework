# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
import json
import csv
import pickle


def get_dir_size(dir_):
    total_size = 0
    for path, dirs, files in os.walk(dir_):
        for f in files:
            total_size += os.path.getsize(os.path.join(path, f))
    return total_size


def save_dir_info(dir_):
    brief = []
    for path, dirs, files in os.walk(dir_):
        for d in dirs:
            brief.append({'obj': d, 'parent': os.path.basename(path), 'obj_type': 'directory',
                         'size': get_dir_size(os.path.join(path, d))})
        for f in files:
            brief.append({'obj': f, 'parent': os.path.basename(path), 'obj_type': 'file',
                         'size': os.path.getsize(os.path.join(path, f))})

    if not os.path.exists('Files'):
        os.makedirs('Files')

    with(
        open('Files/data.json', 'w', encoding='utf-8') as j,
        open('Files/data.csv', 'w', newline='', encoding='utf-8') as c,
        open('Files/data.pickle', 'wb') as p
    ):
        json.dump(brief, j)

        csv_write = csv.DictWriter(c, fieldnames=['obj', 'parent', 'obj_type', 'size'])
        csv_write.writeheader()
        csv_write.writerows(brief)

        pickle.dump(brief, p)


directory = os.getcwd()
save_dir_info(directory)
