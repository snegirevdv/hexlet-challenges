# https://ru.hexlet.io/challenges/python_lists_longest_substring_exercise

def find_longest_length(string: str) -> int:
    substring_lenghts: list[int] = []
    current_str = ''
    charset = {}

    for i, char in enumerate(string):
        if char in current_str:
            substring_lenghts.append(len(current_str))
            current_str = current_str[charset[char] + 1:] + char
        else:
            current_str += char
        charset[char] = i

    substring_lenghts.append(len(current_str))
    return max(substring_lenghts)