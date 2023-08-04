class BasicException(Exception):
    pass


class LevelError(BasicException):
    def __init__(self, u_level, a_level):
        self.u_level = u_level
        self.a_level = a_level

    def __str__(self):
        return f"Insufficient admin's access level <{self.a_level}>! Required level: <{self.u_level}>."


class AccessError(BasicException):
    def __init__(self, u_name, u_id):
        self.u_name = u_name
        self.u_id = u_id

    def __str__(self):
        return f'User with name <{self.u_name}>, id <{self.u_id}> is not in Users List!'


class LevelValueError(BasicException):
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __str__(self):
        return f'User level must be in range {self.min_val} to {self.max_val - 1}!'
