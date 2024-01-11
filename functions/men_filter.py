# https://ru.hexlet.io/challenges/python_functions_count_by_years_exercise

from collections import Counter


def get_men_counted_by_year(users: list[dict]) -> dict:
    men = filter(lambda user: user['gender'] == 'male', users)
    years = map(lambda user: int(user['birthday'][:4]), men)
    return Counter(years)
