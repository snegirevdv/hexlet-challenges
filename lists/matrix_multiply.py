# https://ru.hexlet.io/challenges/python_lists_matrix_multiplication_exercise

def multiply(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    m = len(matrix1)
    n = len(matrix1[0])
    if len(matrix2) != n:
        raise ValueError("Некорректные размеры входных матриц")
    k = len(matrix2[0])

    result: list[list[int]] = []

    for i in range(m):
        current_row: list[int] = []
        for j in range(k):
            current_row.append(sum(matrix1[i][t] * matrix2[t][j] for t in range(n)))
        result.append(current_row)

    return result
