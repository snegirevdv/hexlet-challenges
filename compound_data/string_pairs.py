# https://ru.hexlet.io/challenges/python_compound_data_pairs_on_strings_exercise

from typing import Any


DELIMETER = "\0"


def cons(first: Any, second: Any) -> str:
    return str(first) + DELIMETER + str(second)


def car(pair: str) -> Any:
    return pair.split(DELIMETER)[0]


def cdr(pair: str) -> Any:
    return pair.split(DELIMETER)[1]
