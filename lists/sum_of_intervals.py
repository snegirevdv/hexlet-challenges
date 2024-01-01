# https://ru.hexlet.io/challenges/python_lists_sum_of_intervals_exercise

def sum_of_intervals(intervals: list[list[int]]) -> int:
    counted_nums = []
    for interval in intervals:
        a, b = interval[0], interval[1]
        for num in range(a, b):
            if num not in counted_nums:
                counted_nums.append(num)
    return len(counted_nums)
