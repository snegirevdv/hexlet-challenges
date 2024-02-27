# https://ru.hexlet.io/challenges/python_declarative_programming_probabilities_exercise

def calculate_probabilities(history: list[int]):
    return {
        number: {
            next_number: calculate_probability(number, next_number, history)
            for next_number
            in get_next_numbers_list(number, history)
        } for number in sorted(set(history))
    }


def calculate_probability(number, next_number, history):
    return sum(
        1
        for first, second in zip(history, history[1:])
        if first == number and second == next_number
    ) / history[:-1].count(number)


def get_next_numbers_list(number, history):
    return tuple(
        history[index + 1]
        for index, value in enumerate(history[:-1])
        if value == number
    )
