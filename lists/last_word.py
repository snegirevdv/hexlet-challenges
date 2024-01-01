# https://ru.hexlet.io/challenges/python_lists_length_of_last_word_exercise


def length_of_last_word(text: str) -> int:
    words = text.strip().split()
    return len(words[-1]) if words else 0
