# https://ru.hexlet.io/challenges/python_lists_snail_exercise

def snail_path(matrix: list[list]) -> list:
    if not matrix:
        return []

    result = []

    n = len(matrix)  # высота матрицы
    m = len(matrix[0])  # ширина матрицы
    rows: list[int] = list(range(n - 1, -1, -1))  # массив индексов строк
    columns: list[int] = list(range(m))  # массив индексов столбцов

    # индексы
    i = 0
    j = 0

    while len(result) < m * n:
        for j in columns:
            result.append(matrix[i][j])

        if rows:
            rows.pop()
            rows.reverse()
        else:
            break

        for i in rows:
            result.append(matrix[i][j])

        if columns:
            columns.pop()
            columns.reverse()
        else:
            break

    return result
