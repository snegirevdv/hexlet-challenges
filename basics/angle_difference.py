# https://ru.hexlet.io/challenges/python_basics_angle_difference_exercise


def diff(angle1, angle2) -> int:
    angle1, angle2 = angle1 % 360, angle2 % 360
    dif = abs(angle2 - angle1)
    return min((dif, 360 - dif))
