# https://ru.hexlet.io/challenges/python_basics_happy_ticket_exercise

def get_sum(string: str) -> int:
    return sum(map(int, string))


def is_happy_ticket(num: str) -> bool:
    if len(num) % 2:
        return False
    middle = len(num) // 2
    return get_sum(num[:middle]) == get_sum(num[middle:])
