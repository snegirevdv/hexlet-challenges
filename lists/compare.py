# https://ru.hexlet.io/challenges/python_lists_compare_versions_exercise

def get_parts(version: str) -> list[int]:
    return [int(x) for x in version.split('.')]


def compare_version(version1: str, version2: str) -> int:
    v1_parts = get_parts(version1)
    v2_parts = get_parts(version2) 
    if v1_parts < v2_parts:
        return -1
    if v1_parts > v2_parts:
        return 1
    return 0

