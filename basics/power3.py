# https://ru.hexlet.io/challenges/python_basics_power3_exercise

def is_power_of_three(num):
    i = 1
    while i <= num:
        if i == num:
            return True
        i *= 3
    return False
