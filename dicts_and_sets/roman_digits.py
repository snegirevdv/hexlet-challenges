# https://ru.hexlet.io/challenges/python_dicts_to_roman_exercise

NUMERALS = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def to_roman(num: int) -> str:
    result = ""
    for digit, value in NUMERALS.items():
        while num >= value:
            result += digit
            num -= value
            if num == 0:
                break
    return result


def to_arabic(roman: str) -> int:
    result = 0
    for digit, value in NUMERALS.items():
        if len(digit) == 1 and digit * 4 in roman:
            return False
        while roman.startswith(digit):
            result += value
            roman = roman[len(digit) :]
    if roman:
        return False
    return result
