# https://ru.hexlet.io/challenges/python_declarative_programming_probabilities_exercise

def calculate_probabilities(history: list[int]):
    numbers = sorted(set(history))
    result = {}
    limit = len(history) - 1

    for number in numbers:
        element = {}
        count = history[:limit].count(number)
        for i in range(limit):
            if history[i] == number:
                element[history[i + 1]] = (
                    element.get(history[i + 1], 0) + 1
                    / count
                )
        result[number] = {key: element[key] for key in sorted(element)}

    return result
