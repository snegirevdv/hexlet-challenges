# https://ru.hexlet.io/challenges/python_dicts_query_string_exercise


def build_query_string2(params: dict) -> str:
    result = []
    for key, value in sorted(params.items()):
        result.append(f"{key}={value}")
    return "&".join(result)
