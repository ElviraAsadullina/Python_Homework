import csv


SUBJECTS = ['Latin', 'Anatomy', 'Histology', 'Biophysics', 'Biochemistry', 'Physiology', 'Therapy']
path = 'subjects.csv'


def create_csv(csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\n')
        writer.writerow(line for line in SUBJECTS)


# if __name__ == '__main__':
#     create_csv(path)
