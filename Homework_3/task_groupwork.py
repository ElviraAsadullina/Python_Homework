# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
from functools import reduce

alex = {'Alex': ('tent', 'sleep bag', 'fish rod')}
inna = {'Inna': ('sleep bag', 'food', 'drinks')}
valera = {'Valera': ('sleep bag', 'fish rod', 'bait')}
limit = 1

sked = alex | inna | valera

same_items = set(reduce(set.intersection, (set(v) for v in sked.values())))
print('\nSame items: ' + ', '.join(same_items), end='\n\n' if same_items else 'No same items found')

all_items = [item for friend, items in sked.items() for item in items]
unique_items = set(i for i in all_items if all_items.count(i) == limit)
print('Unique items: ' + ', '.join(unique_items), end='\n\n' if unique_items else 'No unique items found')

selected_items = set(all_items) - same_items - unique_items
if selected_items:
    for friend, items in sked.items():
        if not set(items) & selected_items:
            print(f'Only {friend} has no ' + ', '.join(selected_items))
else:
    print('No items for all but one found')
