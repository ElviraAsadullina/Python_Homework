class BasicException(Exception):
    pass


class SubjectNameError(BasicException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Subject "{self.name}" does not belong to subject-list!'


class SubjectParamsError(BasicException):
    def __init__(self, value, min_value, max_value):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f'Number {self.value} is not between {self.min_value} and {self.max_value}!'
