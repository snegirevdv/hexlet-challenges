# https://ru.hexlet.io/challenges/python_dicts_scrabble_exercise/i

from collections import Counter


# Вариант 1
def scrabble1(symbols: str, word: str) -> bool:
    counter_symbols = Counter(symbols.lower())
    counter_word = Counter(word.lower())
    return counter_word <= counter_symbols


# Вариант 2
def scrabble2(symbols: str, word: str) -> bool:
    counter = Counter(symbols.lower())
    counter.subtract(word.lower())
    for symbol in counter:
        if counter[symbol] < 0:
            return False
    return True


# Вариант 3
def scrabble3(symbols: str, word: str) -> bool:
    counter = Counter(symbols.lower())
    counter.subtract(word.lower())
    return all([counter[symbol] >= 0 for symbol in counter])


def test_scrabble(scrabble):
    assert scrabble("begsdhhtsexoult", "hexlet") is True
    assert scrabble("rkqodlw", "world") is True
    assert scrabble("begsdhhtsexoult", "hexlet") is True
    assert scrabble("katas", "steak") is False
    assert scrabble("scriptjava", "javascript") is True
    assert scrabble("scriptingjava", "javascript") is True
    assert scrabble("scriptjavest", "javascript") is False
    assert scrabble("", "hexlet") is False
    assert scrabble("scriptingjava", "JavaScript") is True


test_scrabble(scrabble1)
test_scrabble(scrabble2)
test_scrabble(scrabble3)
