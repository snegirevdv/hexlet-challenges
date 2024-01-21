# https://ru.hexlet.io/challenges/python_compound_data_triple_exercise


from typing import Any


def make(first: Any, second: Any, third: Any) -> dict[str, Any]:
    return dict(first=first, second=second, third=third)


def get1(triple: dict) -> Any:
    return triple["first"]


def get2(triple: dict) -> Any:
    return triple["second"]


def get3(triple: dict) -> Any:
    return triple["third"]
