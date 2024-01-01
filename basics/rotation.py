# https://ru.hexlet.io/challenges/python_basics_tuple_rotation_exercise

def rotate_left(triple):
    return (*triple[1:], triple[0])


def rotate_right(triple):
    return (triple[-1], *triple[:2])
