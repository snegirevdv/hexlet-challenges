# https://ru.hexlet.io/challenges/python_compound_data_pairs_exercise

def cons(a: int, b: int) -> int:
    return (2 ** a) * (3 ** b)


def car(pair: int) -> int:
    return get_multiplyers_amont(pair, 2)


def cdr(pair: int) -> int:
    return get_multiplyers_amont(pair, 3)


def get_multiplyers_amont(number, multiplyer):
    result = 0

    while not number % multiplyer:
        number /= multiplyer
        result += 1

    return result
