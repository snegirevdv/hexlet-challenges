# https://ru.hexlet.io/challenges/python_dicts_hash_table_exercise/

import zlib
from typing import Any


# Класс Map
class Map(list):
    def __setitem__(self, index, value):
        try:
            super().__setitem__(index, value)
        except IndexError:
            for _ in range(index - len(self) + 1):
                self.append(None)
            super().__setitem__(index, value)

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return None


def make():
    return Map()


# Решение
def get_index(key: str | bytes) -> int:
    return zlib.crc32(key) % 1000


def set_(m: Map, key: str | bytes, value: Any) -> bool:
    index = get_index(key)
    if m[index] and m[index][0] != key:  # проверка коллизии
        return False
    m[index] = (key, value)
    return True


def get_(m: Map, key: str | bytes, default: Any | None = None) -> Any | None:
    index = get_index(key)
    if m[index] is None:
        return default
    if m[index][0] == key:  # проверка коллизии
        return m[index][1]
    return
