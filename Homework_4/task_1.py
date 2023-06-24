# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию, которая
# при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s)
# на None. Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
def change_globals_list():
    globals().update({k[:-1]: v for k, v in globals().items() if k[-1] == 's' and len(k) != 1})
    globals().update({k: None for k, v in globals().copy().items() if k[-1] == 's' and len(k) != 1})
# Не получилось сделать универсальную функцию в одну строку с опционной передачей аргументов [:-1] и None при
# вызове функции. Пыталась в теле функции через *args обозначить нужные/ненужные параметры. Не вышло.


nums = [1, 2, 3]
s = 'My string'
sked = ('Sergey', 'Olga')
booleans = {'True', 'False'}

change_globals_list()

print(f'{nums = }\n{s = }\n{sked = }\n{booleans = }\n')
print(f'{num = }\n{s = }\n{sked = }\n{boolean = }')
