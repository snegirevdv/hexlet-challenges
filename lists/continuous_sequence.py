# https://ru.hexlet.io/challenges/python_lists_ascending_sequence_exercise


def is_continuous_sequence(sequence: list[int]) -> bool:
    if len(sequence) <= 1:
        return False
    for num1, num2 in zip(sequence, sequence[1:]):
        if num2 - num1 != 1:
            return False
    return True
