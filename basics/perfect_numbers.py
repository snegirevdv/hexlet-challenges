# https://ru.hexlet.io/challenges/python_basics_perfect_numbers_exercise

def is_perfect(num):
    if num <= 0:
        return False
    result = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result += i
    return result == num
