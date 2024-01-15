# https://ru.hexlet.io/challenges/python_functions_filter_anagrams_exercise

from collections.abc import Iterable, Collection


def filter_anagrams(pattern: Collection, iterable: Iterable) -> list:
    result = []
    for element in iterable:
        if is_anagram(element, pattern):
            result.append(element)
    return result


def is_anagram(first: Collection, second: Collection) -> bool:
    elements = {}
    if len(first) != len(second):
        return False
    for element1, element2 in zip(first, second):
        elements[element1] = elements.get(element1, 0) + 1
        elements[element2] = elements.get(element2, 0) - 1
    for value in elements.values():
        if value != 0:
            return False
    return True
