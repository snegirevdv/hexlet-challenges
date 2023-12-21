# https://ru.hexlet.io/challenges/python_dicts_dictionaries_merge_exercise

from collections import defaultdict


def merged(dicts: list[dict]) -> defaultdict:
    result = defaultdict(set)
    for d in dicts:
        for key, value in d.items():
            result[key].add(value)
    return result
