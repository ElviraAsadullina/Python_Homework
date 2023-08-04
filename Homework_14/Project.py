import json
import sys
from colorama import Fore

from Exceptions import AccessError, LevelError
from User import User


class Project:
    # PATH = 'users.json'

    @classmethod
    def get_users_from_json(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            my_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        users_lst = []
        for level, users in my_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                users_lst.append(user)
        return Project(users_lst)

    def __init__(self, users_lst=None):
        if users_lst is None:
            self.users_lst = []
        self.users_lst = users_lst
        self.admin = None

    def login(self, other):
        for user in self.users_lst:
            if user == other:
                other.level = user.level
                self.admin = other
                break
        else:
            raise AccessError(other.name, other.u_id)

    def add_user(self, other):
        if other.level < self.admin.level:
            raise LevelError(other.level, self.admin.level)
        self.users_lst.append(other)

    def remove_user(self, other):
        if other not in self.users_lst:
            raise AccessError(other.name, other.u_id)
        elif other.level < self.admin.level:
            raise LevelError(other.level, self.admin.level)
        self.users_lst.remove(other)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open('users.json', 'w', encoding='utf-8') as f:
            my_dict = {}
            for user in self.users_lst:
                if user.level not in my_dict:
                    my_dict[user.level] = {}
                my_dict[user.level][user.u_id] = user.name
            json.dump(my_dict, f)

    def __str__(self):
        return f'Project {self.__dict__}'

    def run(self):
        print('\n\33[7m' + 'Please login to access system' + '\033[0m\n')
        u = User(input('Input your name: '), int(input('Input your id: ')))
        Project.login(self, u)
        print(Fore.GREEN + f'\nSuccessfully logged in!' + Fore.RESET)
        print(f'YOU ARE ADMIN NOW.')
        while True:
            print('\n\33[7m' + 'MAIN MENU' + '\033[0m\n\n'
                                             '1 - Add user\n'
                                             '2 - Delete user\n'
                                             '3 - Get users list\n'
                                             '4 - Quit\n')
            choice = input('Choose action: ')
            match choice:
                case '1':
                    u_1 = User(input("Input user's name: "), int(input("Input user's id: ")),
                               int(input("Input user's level: ")))
                    Project.add_user(self, u_1)
                    print(Fore.GREEN + f'{u_1} added successfully!' + Fore.RESET)
                case '2':
                    u_2 = User(input("Input user's name: "), int(input("Input user's id: ")),
                               int(input("Input user's level: ")))
                    Project.remove_user(self, u_2)
                    print(Fore.GREEN + f'{u_2} removed successfully!' + Fore.RESET)
                case '3':
                    print('USERS LIST:')
                    for user, number in enumerate(self.users_lst, 1):
                        print('{0}. {1}'.format(user, number))
                case '4':
                    print(Fore.GREEN + '\nUsers List saved to file!' + Fore.RESET)
                    print('Have a nice day!')
                    sys.exit()
                case _:
                    print(Fore.RED + 'Invalid choice! Please try again!' + Fore.RESET)
