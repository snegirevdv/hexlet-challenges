# https://ru.hexlet.io/challenges/python_functions_functional_enlarge_image_exercise

# Линтер закономерно ругается на такие функции, потому что
# обычно именованные функции не делаются с помощью лямбд.
from functools import reduce
from operator import add

curry = lambda f: lambda x: lambda y: f(x, y)  # noqa: E731
compose = lambda f: lambda g: lambda x: f(g(x))  # noqa: E731

pair = lambda x: [x, x]  # noqa: E731
dup = lambda x: x + x  # noqa: E731

TypeMatrix = list[list[str]]


def enlarge(matrix: TypeMatrix) -> TypeMatrix:
    symbol_duplicator = curry(map)(dup)
    stringificator = compose("".join)(symbol_duplicator)
    map_creator = curry(map)(stringificator)
    convertor_to_list = compose(list)(map_creator)
    row_duplicator = curry(reduce)(add)
    return convertor_to_list(row_duplicator(map(pair, matrix)))
