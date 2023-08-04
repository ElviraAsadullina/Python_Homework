from Exceptions import LevelValueError


class LevelDescriptor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value is not None and value not in range(self.min_value, self.max_value):
            raise LevelValueError(self.min_value, self.max_value)
        setattr(instance, self.param_name, value)


class User:
    level = LevelDescriptor(1, 8)

    def __init__(self, name, user_id, level=None):
        self.name = name
        self.u_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.u_id == other.u_id

    def __str__(self):
        return f'User {self.name} with id <{self.u_id}>, level <{self.level}>'

    def __repr__(self):
        return f'User {self.name=}, {self.u_id=}, {self.level=}'
