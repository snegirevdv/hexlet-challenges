# https://ru.hexlet.io/challenges/python_lists_chunk_exercise

from typing import Sequence


def chunked(step: int, sequence: Sequence) -> list[Sequence]:
    result = []
    for i in range(0, len(sequence), step):
        result.append(sequence[i: i + step])
    return result
