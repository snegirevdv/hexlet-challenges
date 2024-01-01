# https://ru.hexlet.io/challenges/python_lists_enlarge_image_exercise

def enlarge(image: list[str], n: int = 2) -> list[str]:
    result = []
    for row in image:
        new_row = ''.join(symbol * n for symbol in row)
        result.extend([new_row] * n)
    return result
