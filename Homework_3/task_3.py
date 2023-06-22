# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно
# вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import itertools

stuff_roll = {'tent': 20, 'sleep bags': 6, 'fish rods': 2, 'food': 5, 'drinks': 3}
sack_capacity = 30

result = [kit for weight in range(len(stuff_roll.values()), 0, -1)
          for kit in itertools.combinations(stuff_roll.keys(), weight)
          if sum(map(stuff_roll.get, kit)) <= sack_capacity]

result.sort(key=len)
for res in result:
    print(*res, sep=', ', end='\n')
