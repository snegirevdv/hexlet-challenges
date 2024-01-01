# https://ru.hexlet.io/challenges/python_dicts_scrabble_exercise/i

from collections import Counter

def scrabble1(symbols: str, word: str) -> bool:
    counter_symbols = Counter(symbols.lower())
    counter_word = Counter(word.lower())
    return counter_word <= counter_symbols
