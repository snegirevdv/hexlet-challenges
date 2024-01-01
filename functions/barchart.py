# https://ru.hexlet.io/challenges/python_functions_bar_chart_exercise


def get_cell(row: int, column: int) -> str:
    if column < 0 and 0 > row >= column:
        return "#"
    if column > 0 and 0 < row <= column:
        return "*"
    return " "


def get_row(row: int, columns: list[int]) -> str:
    return "".join(get_cell(row, column) for column in columns)


def barchart(columns: list[int]) -> str:
    top = max(columns)
    bottom = min(columns)
    return "\n".join(
        get_row(row, columns) for row in range(top, bottom - 1, -1) if row != 0
    )
