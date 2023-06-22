# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
import collections

nums = [11, 12, 11, 13, 14, 13, 15, 13, 16, 12]
limit = 1

repeating_nums = [i for i, count in collections.Counter(nums).items() if count > limit]

print(repeating_nums)
