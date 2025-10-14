from text_module import normalize, tokenize, count_freq, top_n 

def run_tests():
    print("=== normalize ===")
    print(normalize("ПрИвЕт\nМИр\t"), "→", "привет мир")
    print(normalize("ёжик, Ёлка"), "→", "ежик, елка")
    print(normalize("Hello\r\nWorld"), "→", "hello world")
    print(normalize("  двойные   пробелы  "), "→", "двойные пробелы")

    print("\n=== tokenize ===")
    print(tokenize("привет мир"), "→", ["привет", "мир"])
    print(tokenize("hello,world!!!"), "→", ["hello", "world"])
    print(tokenize("по-настоящему круто"), "→", ["по-настоящему", "круто"])
    print(tokenize("2025 год"), "→", ["2025", "год"])
    print(tokenize("emoji 😀 не слово"), "→", ["emoji", "не", "слово"])

    print("\n=== count_freq + top_n ===")
    tokens1 = ["a", "b", "a", "c", "b", "a"]
    freq1 = count_freq(tokens1)
    print(freq1, "→", {"a": 3, "b": 2, "c": 1})
    print(top_n(freq1, n=2), "→", [("a", 3), ("b", 2)])

    tokens2 = ["bb", "aa", "bb", "aa", "cc"]
    freq2 = count_freq(tokens2)
    print(freq2, "→", {"aa": 2, "bb": 2, "cc": 1})
    print(sorted(freq2.items(), key=lambda x: (-x[1], x[0]))[:2], "→", [("aa", 2), ("bb", 2)])


if __name__ == "__main__":
    run_tests()