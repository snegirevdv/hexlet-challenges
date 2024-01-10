# https://ru.hexlet.io/challenges/python_functions_ip2int32_exercise


from collections import deque


def ip2int(ip: str) -> int:
    segments = map(int, ip.split('.'))
    return sum(
        segment * 256 ** (3 - index)
        for index, segment
        in enumerate(segments)
    )


def int2ip(number: int) -> str:
    segments = deque()

    for _ in range(4):
        segments.appendleft(str(number % 256))
        number //= 256

    return '.'.join(segments)
