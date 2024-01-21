# https://ru.hexlet.io/challenges/python_functions_find_nearest_exercise

from typing import Optional


def get_distance(number1: int, number2: int) -> int:
    return abs(number1 - number2)


def find_index_of_nearest(number_to_find: int, numbers: list) -> Optional[int]:
    if numbers:
        min_distance_value = get_distance(number_to_find, numbers[0])
        min_distance_index = 0
        for index, number in enumerate(numbers[1:]):
            if get_distance(number_to_find, number) < min_distance_value:
                min_distance_index = index
                min_distance_value = number

        return min_distance_index
