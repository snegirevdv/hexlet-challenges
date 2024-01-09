# https://ru.hexlet.io/challenges/python_functions_nrzi_exercise/instance

def decode(signal: str) -> str:
    decoded_1 = signal.replace("|_", "1").replace("|¯", "1")
    return "".join(char if char == "1" else "0" for char in decoded_1)
