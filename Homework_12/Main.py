from Homework_12.Student import Student
from Homework_12.modules.module_csv import create_csv, path

create_csv(path)

s_1 = Student('Petrova', 'Inna', 'Sergeevna')
s_2 = Student('Antonov', 'Oleg', 'Ivanovich')

s_1.add_mark('Therapy', 5)
s_1.add_mark('Latin', 4)
s_1.add_mark('Histology', 5)
s_1.add_mark('Histology', 5)
# s_1.add_mark('Maths', 5)
s_2.add_mark('Physiology', 3)
s_2.add_mark('Biophysics', 2)
s_2.add_mark('Biophysics', 3)
s_2.add_mark('Latin', 5)

s_1.add_test_score('Anatomy', 80)
s_1.add_test_score('Anatomy', 100)
# s_1.add_test_score('Maths', 100)
s_2.add_test_score('Biochemistry', 20)
s_2.add_test_score('Biochemistry', 30)

print(s_1)
print(f'Average mark for student {s_1.full_name} = {s_1.average_mark()}')
print(f'Average subject wise score for student {s_1.full_name} = {s_1.average_test_score("Anatomy")}\n')
print(s_2)
print(f'Average mark for student {s_2.full_name} = {s_2.average_mark()}')
print(f'Average subject wise score for student {s_2.full_name} = {s_2.average_test_score("Biochemistry")}')
