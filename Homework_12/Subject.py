from Homework_12.Exceptions import SubjectParamsError


class Subject:
    MIN_MARK = 2
    MAX_MARK = 5
    MIN_TEST_SCORE = 0
    MAX_TEST_SCORE = 100

    def __init__(self, name):
        self.name = name
        self.marks = []
        self.test_scores = []

    def add_mark(self, mark):
        if mark not in range(Subject.MIN_MARK, Subject.MAX_MARK + 1):
            raise SubjectParamsError(mark, Subject.MIN_MARK, Subject.MAX_MARK)
        self.marks.append(mark)

    def add_test_score(self, test_score):
        if test_score not in range(Subject.MIN_TEST_SCORE, Subject.MAX_TEST_SCORE + 1):
            raise SubjectParamsError(test_score, Subject.MIN_TEST_SCORE, Subject.MAX_TEST_SCORE)
        self.test_scores.append(test_score)

    def average_mark(self):
        return None if len(self.marks) == 0 else sum(self.marks) / len(self.marks)

    def average_test_score(self):
        return None if len(self.test_scores) == 0 else sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        return f'Subject {self.__dict__}'

    def __repr__(self):
        return f'(marks={self.marks}, test_scores={self.test_scores})'


# if __name__ == '__main__':
#     s_1 = Subject('Therapy')
#     print(s_1)
#     s_1.add_mark(2)
#     s_1.add_mark(5)
#     s_1.add_test_score(100)
#     print(s_1)
