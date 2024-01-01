# https://ru.hexlet.io/challenges/python_lists_pascal_triangle_exercise

def fact(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def triangle(n):
    if n == 0:
        return [1]
    result = [1, n]
    factorials = {i: fact(i) for i in range(n + 1)}
    for m in range(2, n + 1):
        result.append(int(factorials[n] / (factorials[m] * factorials[n - m])))
    return result
