# https://ru.hexlet.io/challenges/python_functions_ipv6_validator_exercise

from string import hexdigits


def is_valid_ipv6(ip: str) -> bool:
    ip = ip.lower()
    segments = ip.split(":")
    good_symbols = hexdigits + ":"

    return (
        ip.count("::") <= 1
        and ":::" not in ip
        and not ("::" not in ip and len(segments) != 8)
        and not ("::" in ip and len(segments) > 8)
        and all(map(lambda x: x in good_symbols, ip))
        and all(map(lambda x: len(x) <= 4, segments))
        and not (ip[-1] == ":" and ip[-2] != ":")
        and not (ip[0] == ":" and ip[1] != ":")
    )
