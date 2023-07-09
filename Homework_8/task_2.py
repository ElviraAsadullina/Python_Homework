# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle

with open('Task_1/users_updated.csv', 'r', newline='', encoding='utf-8') as f:
    csv_read = csv.reader(f, delimiter='|')
    lst = [line for i, line in zip(range(4), csv_read)]
my_dict = {k: v for k, *v in zip(*lst)}
print(pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL))
