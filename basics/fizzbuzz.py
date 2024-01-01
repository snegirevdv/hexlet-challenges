# https://ru.hexlet.io/challenges/python_basics_fizzbuzz_exercise


def get_number_or_fizzbuzz(number):
    result = ""
    if not number % 3:
        result += "Fizz"
    if not number % 5:
        result += "Buzz"
    return result or str(number)


def fizz_buzz(begin, end):
    return " ".join(get_number_or_fizzbuzz(i) for i in range(begin, end + 1))
