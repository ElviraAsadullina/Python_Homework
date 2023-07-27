# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов
# вместе взятых.
import csv
from Homework_12.modules.module_csv import path
from Homework_12.Exceptions import SubjectNameError
from Homework_12.Subject import Subject


class StudentDescriptor:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError('Personal credentials should start with capital and can only contain letters!')
        setattr(instance, self.param_name, value)


class Student:
    first_name = StudentDescriptor()
    last_name = StudentDescriptor()
    middle_name = StudentDescriptor()

    def __init__(self, last_name, first_name, middle_name):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.subjects = {}
        with open(path, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                subject_name = row[0]
                self.subjects[subject_name] = Subject(subject_name)

    @property
    def full_name(self):
        return ' '.join((self.last_name, self.first_name, self.middle_name))

    def add_mark(self, subject_name, mark):
        if subject_name not in self.subjects:
            raise SubjectNameError(subject_name)
        self.subjects[subject_name].add_mark(mark)

    def add_test_score(self, subject_name, test_score):
        if subject_name not in self.subjects:
            raise SubjectNameError(subject_name)
        self.subjects[subject_name].add_test_score(test_score)

    def average_mark(self):
        marks = []
        for subject in self.subjects.values():
            marks.extend(subject.marks)
        return None if len(marks) == 0 else round(sum(marks) / len(marks), 2)

    def average_test_score(self, subject_name=None):
        if subject_name is not None:
            if subject_name not in self.subjects:
                raise SubjectNameError(subject_name)
            return self.subjects[subject_name].average_test_score()
        else:
            test_results = []
            for subject in self.subjects.values():
                test_results.extend(subject.test_scores)
            return None if len(test_results) == 0 else round(sum(test_results) / len(test_results), 2)

    def __str__(self):
        return f'Student: {self.full_name}, Progress: {self.subjects}'
