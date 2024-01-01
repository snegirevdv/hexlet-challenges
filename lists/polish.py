# https://ru.hexlet.io/challenges/python_lists_reverse_polish_notation_exercise

from operator import add, sub, mul, truediv
from typing import Callable

OPERATIONS: dict[str, Callable] = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
}


def make_operation(stack: list[int], operator: str):
    operation = OPERATIONS[operator]
    operand_2 = stack.pop()
    opernad_1 = stack.pop()
    stack.append(operation(opernad_1, operand_2))


def rpn_calc(expression: list[int | str]) -> int:
    stack: list[int] = []
    for item in expression:
        if isinstance(item, int):
            stack.append(item)
        else:
            make_operation(stack, item)
    if len(stack) == 1:
        return stack[0]
