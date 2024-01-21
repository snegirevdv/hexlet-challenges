# https://ru.hexlet.io/challenges/python_functions_function_composition_exercise

from typing import Callable


def compose(func1: Callable, func2: Callable) -> Callable:
    def inner(*args, **kwargs):
        return func1(func2(*args, **kwargs))
    return inner
