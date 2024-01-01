# https://ru.hexlet.io/challenges/python_lists_moneybox_exercise

from collections import Counter


def visualize(coins: tuple[int], bar_char: str = '₽') -> str:
    """Visualize money in a money box."""
    counter = Counter(coins)
    result_list: list[str] = []

    while len(result_list) < max(counter.values()) + 1:
        row = []
        for _, count in sorted(counter.items()):
            if count > len(result_list):
                row.append(f"{bar_char * 2:<2}")
            elif count == len(result_list):
                row.append(f"{count:<2}")
            else:
                row.append(f"{'':<2}")
        result_list.append(" ".join(row))

    result_list.reverse()
    summary = [f"{coin:<2}" for coin in sorted(counter)]
    result_list.append(" ".join(summary))
    result_list.insert(-1, "-" * max(map(len, result_list)))

    return "\n".join(result_list)
