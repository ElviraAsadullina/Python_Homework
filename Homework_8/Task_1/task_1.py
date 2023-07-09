# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи
# словаря для заголовков столбца из переданного файла.
import csv
import pickle


def from_pickle_to_csv(pickle_file):
    with open(pickle_file, 'rb') as f1:
        my_list = pickle.load(f1)
    my_dict = {}
    for dictionary in my_list:
        for k, v in dictionary.items():
            my_dict.setdefault(k, []).append(v)

    with open('users_updated.csv', 'w', newline='', encoding='utf-8') as f2:
        csv_write = csv.writer(f2, delimiter='|')
        csv_write.writerow(my_dict.keys())
        csv_write.writerows(zip(*my_dict.values()))


from_pickle_to_csv('users_updated.pickle')
