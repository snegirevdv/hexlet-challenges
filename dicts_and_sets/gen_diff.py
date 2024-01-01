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
