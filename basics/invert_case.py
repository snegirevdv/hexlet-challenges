# https://ru.hexlet.io/challenges/python_basics_invert_case_exercise

def invert_case(text):
    result = ""
    for char in text:
        if char == char.lower():
            result += char.upper()
        elif char == char.upper():
            result += char.lower()
    return result
