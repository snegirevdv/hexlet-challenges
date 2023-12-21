# https://ru.hexlet.io/challenges/python_dicts_operations_exercise


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
        "six": "changed",
        "five": "unchanged",
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
