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


# print(tokenize("  Hello, World! This is a test.  "))