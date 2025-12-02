import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/lib')))
from text_module import normalize, tokenize, count_freq, top_n

@pytest.mark.parametrize(
    "src, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка!", "ежик, елка!"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("\t\n  ", ""),                  # only whitespace
        ("", ""),                         # empty
        ("@@@TEST@@@", "@@@test@@@"),     # punctuation preserved
    ],
)
def test_normalize(src: str, expected: str):
    assert normalize(src) == expected

@pytest.mark.parametrize(
    "src, expected",
    [
        ("hello world", ["hello", "world"]),
        ("один, два! три?", ["один", "два", "три"]),
        ("mix: A1 B2 C3", ["mix", "a1", "b2", "c3"]),
        ("", []),
        ("   lone   ", ["lone"]),
        ("!!!???,,,", []),
        ("Hello\nworld\tagain", ["hello", "world", "again"]),
    ],
)
def test_tokenize(src: str, expected: list[str]):
    assert tokenize(src) == expected

@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),
        (["x"], {"x": 1}),
        (["same", "same", "same"], {"same": 3}),
    ],
)
def test_count_freq(tokens: list[str], expected: dict[str, int]):
    assert count_freq(tokens) == expected

def test_top_n_basic():
    freq = {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_n_tie_breaker():
    freq = {"beta": 2, "alpha": 2, "gamma": 1}
    assert top_n(freq, 3) == [
        ("alpha", 2),
        ("beta", 2),
        ("gamma", 1),
    ]


def test_top_n_empty():
    assert top_n({}, 5) == []


def test_top_n_n_greater_than_length():
    freq = {"x": 10}
    assert top_n(freq, 10) == [("x", 10)]
