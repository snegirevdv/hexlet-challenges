# https://ru.hexlet.io/challenges/python_declarative_programming_stream_chunking_exercise

from collections.abc import Iterable, Iterator


def ichunks(size: int, iterable: Iterable) -> Iterator:
    iterator = iter(iterable)

    while True:
        try:
            yield [next(iterator) for _ in range(size)]
        except StopIteration:
            return
