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