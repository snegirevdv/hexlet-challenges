# https://ru.hexlet.io/challenges/python_lists_matrix_transposing_exercise


def transposed(matrix: list[list[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    width = len(matrix[0])
    length = len(matrix)

    for j in range(width):
        row: list[int] = [matrix[i][j] for i in range(length)]
        result.append(row)

    return result
