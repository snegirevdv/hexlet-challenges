from collections import Counter

from collections.abc import Callable


def histo1(rounds_count: int, roll_die: Callable) -> str:
    rolls = (roll_die() for _ in range(rounds_count))
    stat = Counter(rolls)
    lines = map(
        lambda i: f"{i}|" + f"{'#' * stat[i]} {stat[i]}" * bool(stat[i]),
        range(1, 7)
    )
    return "\n".join(lines)


def histo2(rounds_count: int, roll_die: Callable) -> str:
    stat = [0] * 6
    result = []
    for _ in range(rounds_count):
        roll = roll_die()
        stat[roll - 1] += 1
    for index, count in enumerate(stat):
        result.append(
            f"{index + 1}|{('#' * count + ' ' + str(count)) * bool(count)}")
    return "\n".join(result)
