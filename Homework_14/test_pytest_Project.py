# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import json
from tempfile import NamedTemporaryFile
import pytest

from Exceptions import AccessError, LevelError, LevelValueError
from User import User
from Project import Project


@pytest.fixture(scope='function')
def temp_file():
    with NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
        f.write(json.dumps({
            1: {
                '1': 'test1',
                '2': 'test2'
            },
            2: {
                '3': 'test3',
                '4': 'test4'
            }
        }))
        f.flush()
        yield f.name


@pytest.fixture(scope='function')
def project(temp_file):
    return Project.get_users_from_json(temp_file)


def test_level_value_error():
    with pytest.raises(LevelValueError):
        User('test', 1, 8)


def test_users_equal():
    u_1 = User('test', 1, 5)
    u_2 = User('test', 1, 5)
    assert u_1 == u_2


def test_get_users_from_json(project, temp_file):
    assert len(project.users_lst) == 4


def test_login_if_user_in_list(project):
    u_1 = User('test1', 1, 1)
    project.login(u_1)
    assert project.admin == u_1


def test_login_if_user_not_in_list(project):
    with pytest.raises(AccessError):
        u_1 = User('test', 1, 1)
        project.login(u_1)


def test_add_user_success(project):
    adm = User('test1', 1, 1)
    user_to_add = User('test', 2, 1)
    project.login(adm)
    project.add_user(user_to_add)
    assert user_to_add in project.users_lst


def test_add_user_fail(project):
    with pytest.raises(LevelError):
        adm = User('test3', 3, 2)
        user_to_add = User('test', 2, 1)
        project.login(adm)
        project.add_user(user_to_add)


def test_remove_user_success(project):
    adm = User('test1', 1, 1)
    user_to_del = User('test2', 2, 1)
    project.login(adm)
    project.remove_user(user_to_del)
    assert user_to_del not in project.users_lst


def test_remove_user_fail(project):
    with pytest.raises(LevelError):
        adm = User('test4', 4, 2)
        user_to_del = User('test1', 1, 1)
        project.login(adm)
        project.remove_user(user_to_del)


def test_remove_user_invalid_data(project):
    with pytest.raises(AccessError):
        adm = User('test1', 1, 1)
        user_to_del = User('test', 1, 1)
        project.login(adm)
        project.remove_user(user_to_del)
