# https://ru.hexlet.io/challenges/python_dicts_query_string_exercise

# Напишите функцию build_query_string, которая принимает на вход словарь
# с параметрами и возвращает строку запроса, сформированную из этих параметров.

# Вариант 1
def build_query_string1(params: dict) -> str:
    result = (f"{key}={value}" for key, value in sorted(params.items()))
    return "&".join(result)


# Вариант 2
def build_query_string2(params: dict) -> str:
    result = []
    for key, value in sorted(params.items()):
        result.append(f"{key}={value}")
    return "&".join(result)


def test_build_query_string(build_query_string):
    assert build_query_string({}) == ''
    assert build_query_string({'page': 1}) == 'page=1'
    assert build_query_string({'per': 10, 'page': 1}) == 'page=1&per=10'
    assert build_query_string(
        {
            'a': 10,
            's': 'Wow',
            'd': 3.2,
            'z': '89',
        },
    ) == 'a=10&d=3.2&s=Wow&z=89'


test_build_query_string(build_query_string1)
test_build_query_string(build_query_string2)
