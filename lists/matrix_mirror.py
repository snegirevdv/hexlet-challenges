# https://ru.hexlet.io/challenges/python_lists_matrix_mirroring_exercise

def mirror_matrix(matrix: list[list]) -> list[list]:
    width = 0 if not matrix else len(matrix[0])
    middle = width // 2
    lenght = len(matrix)
    for i in range(lenght):
        for j in range(middle):
            matrix[i][width - j - 1] = matrix[i][j]
