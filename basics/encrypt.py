# https://ru.hexlet.io/challenges/python_basics_encrypt_exercise


def encrypt(text):
    result = ""
    i = 0
    while i < len(text) - 1:
        result += text[i + 1] + text[i]
        i += 2
    if len(text) % 2 == 1:
        result += text[-1]
    return result
