# https://ru.hexlet.io/challenges/python_basics_line_classification_exercise


def is_degenerated(line):
    return line[0] == line[1]


def is_vertical(line):
    return not is_degenerated(line) and line[0][0] == line[1][0]


def is_horizontal(line):
    return not is_degenerated(line) and line[0][1] == line[1][1]


def is_inclined(line):
    return not (is_degenerated(line)
                or is_vertical(line)
                or is_horizontal(line))
