# https://ru.hexlet.io/challenges/python_declarative_programming_length_frequences_exercise

from collections.abc import Iterable
import itertools


def length_frequencies(iterable: Iterable[str]) -> dict[int, int]:
    return {
        length: len(list(count))
        for length, count
        in itertools.groupby(
            sorted(iterable, key=len),
            key=len
        )
    }
