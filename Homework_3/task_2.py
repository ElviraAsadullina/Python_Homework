# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.
import re
from collections import Counter

txt = re.findall(r'\w+', open('counter_objects.txt').read().lower())
count = 10

print(';\n'.join(f"'{k}': {v} times" for k, v in Counter(txt).most_common(count)), end='.')
