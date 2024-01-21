# https://ru.hexlet.io/challenges/python_functions_same_parity_exercise

def same_parity_filter(array: list[int]) -> list[int]:
    if not array:
        return array

    parity = array[0] % 2

    return list(filter(lambda x: x % 2 == parity, array))
