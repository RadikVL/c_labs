### Python BIVT-25-5 ЛР2 — Коллекции и матрицы
---

#### text_module.py
``` python
# fuckn modules for text operations - normalize, tokenize, count_freq, top_n.
from collections import Counter
import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст:
    - приводит к нижнему регистру (если casefold=True)
    - заменяет 'ё' на 'е' (если yo2e=True)
    - удаляет символы перевода строки и возврата каретки
    """
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    text = text.replace('\r', '')
    text = text.replace('\n', '')
    return text

def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на токены (слова), включая дефисные слова.
    Токен определяется как последовательность букв, цифр и подчёркиваний, возможно содержащая дефисы внутри слова.
    """
    pattern = r"\w+(?:-\w+)*"
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает частоту каждого токена в списке.
    Возвращает словарь, где ключи - токены, а значения - их частоты.
    """
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает список из n наиболее частых токенов и их частот.
    Список отсортирован по убыванию частоты.
    """
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]
    return list(st)
```

#### text_stats.py
``` python
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib')))
from text_module import normalize, tokenize, count_freq, top_n

table_MOD = True
# table_MOD = False


stdin_text = sys.stdin.readline()
normalized_text = normalize(stdin_text)
tokens = tokenize(normalized_text)
freq = count_freq(tokens)
top5 = top_n(freq, 5)

print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(set(tokens))}')

if table_MOD:
    print('Таблица частот:')
    print(' ')
    items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    max_word_len = max(len(word) for word, _ in items) if items else 5
    header = f'{{:<{max_word_len}}} | {{:>7}}'.format('слово', 'частота')
    print(header)
    print('-' * (max_word_len + 10))
    for word, count in items:
        print(f'{word:<{max_word_len}} | {count:>7}')
else:
    print('Топ-5:')
    print('\n'.join(f'{word}: {count}' for word, count in freq.items()))
```

### Here is all tests for every module:
![](/images/lab03/all_tests.png)

### Image of text_stats.py output:
(table_MOD = True):
![](/images/lab03/test_image.png)