# https://ru.hexlet.io/challenges/python_declarative_programming_intersperse_exercise

from typing import Iterable, Iterator


def intersperse(iterable: Iterable, separator: str | int) -> Iterator:
    is_first = True

    for element in iterable:
        if is_first:
            is_first = False
        else:
            yield separator

        yield element
