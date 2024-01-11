# https://ru.hexlet.io/challenges/python_functions_filter_anagrams_exercise

from collections import Counter
from collections.abc import Iterable


def filter_anagrams(word: str, iterable: Iterable) -> list:
    pattern = Counter(pattern)
    return list(filter(lambda x: Counter(x) == word, iterable))
