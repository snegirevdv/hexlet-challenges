# https://ru.hexlet.io/challenges/python_lists_hamming_weight_exercise


def hamming_weight(num: int) -> int:
    bin_num = f"{num:b}"
    return bin_num.count("1")
