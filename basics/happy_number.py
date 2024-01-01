# https://ru.hexlet.io/challenges/python_basics_happy_numbers_exercise


def sum_of_square_digits(number):
    return sum(int(x) ** 2 for x in str(number))


def is_happy_number(num):
    for _ in range(10):
        num = sum_of_square_digits(num)
        if num == 1:
            return True
    return False
