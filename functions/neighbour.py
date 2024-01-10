# https://ru.hexlet.io/challenges/python_functions_find_nearest_exercise

from typing import Optional


def find_index_of_nearest(number_to_find: int, numbers: list) -> Optional[int]:
    if numbers:
        distances = tuple(abs(number - number_to_find) for number in numbers)
        return distances.index(min(distances))
