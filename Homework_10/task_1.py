# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
class Pets:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_info(self):
        return f'Name: {self.name}; Weight: {self.weight}'


class Dog(Pets):
    def __init__(self, name, weight, hair_length):
        super().__init__(name, weight)
        self.hair_length = hair_length

    def get_info(self):
        return super().get_info() + f'; Hair length: {self.hair_length}'


class Parrot(Pets):
    def __init__(self, name, weight, wingspan):
        super().__init__(name, weight)
        self.wingspan = wingspan

    def get_info(self):
        return super().get_info() + f'; Wingspan: {self.wingspan}'


class Fish(Pets):
    def __init__(self, name, weight, fin_color):
        super().__init__(name, weight)
        self.fin_color = fin_color

    def get_info(self):
        return super().get_info() + f'; Fin color: {self.fin_color}'


class Factory:
    @staticmethod
    def build_instance(cls_name, *args, **kwargs):
        if cls_name not in globals():
            raise ValueError(f'Class "{cls_name}" not found')
        cls = globals()[cls_name]
        return cls(*args, **kwargs)


correct_instance_1 = Factory.build_instance('Fish', 'goldfish', 0.2, 'orange')
correct_instance_2 = Factory.build_instance('Dog', 'husky', 35, 10)
# Создаем экземпляр несуществующего класса, чтобы убедиться, что выйдет ошибка по строке 44:
# incorrect_instance_1 = Factory.build_instance('Cat', 'sphinx', 3, 0.3)

if __name__ == '__main__':
    print(correct_instance_1.__dict__)
    print(correct_instance_2.__dict__)
    # print(incorrect_instance_1.__dict__)
