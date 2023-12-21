# https://ru.hexlet.io/challenges/python_dicts_operations_exercise

# Реализуйте функцию gen_diff, которая сравнивает два словаря и возвращает
# результат сравнения в виде словаря. Ключами результирующего словаря будут
# все ключи из двух входящих, а значением строка с описанием отличий: #
# added, deleted, changed или unchanged.

# added — ключ отсутствовал в первом словаре, но был добавлен во второй
# deleted — ключ был в первом словаре, но отсутствует во втором
# changed — ключ присутствовал и в первом и во втором словаре, но значения отличаются
# unchanged — ключ присутствовал и в первом и во втором словаре с одинаковыми значениями


def gen_diff(dict1: dict, dict2: dict) -> dict:
    keys = set(dict1) | set(dict2)
    result = dict.fromkeys(keys)
    for key in keys:
        if key not in dict1:
            result[key] = "added"
        elif key not in dict2:
            result[key] = "deleted"
        elif dict1[key] != dict2[key]:
            result[key] = "changed"
        else:
            result[key] = "unchanged"
    return result


def test_gen_diff_with_empty_dict():
    assert gen_diff({}, {"two": "own"}) == {"two": "added"}
    assert gen_diff({"one": "eon"}, {}) == {"one": "deleted"}


def test_gen_diff():
    assert gen_diff(
        {"three": "eerht"},
        {"four": "ruof"},
    ) == {
        "three": "deleted",
        "four": "added",
    }

    assert gen_diff(
        {"five": 5, "six": 6},
        {"six": "xis", "five": 5},
    ) == {
        "six": 'changed',
        "five": 'unchanged',
    }

    assert gen_diff(
        {"seven": "neves"},
        {"eighth": True},
    ) == {
        "seven": "deleted",
        "eighth": "added",
    }

test_gen_diff_with_empty_dict()
test_gen_diff()
