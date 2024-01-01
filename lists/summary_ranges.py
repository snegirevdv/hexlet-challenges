# https://ru.hexlet.io/challenges/python_lists_summary_ranges_exercise


def summary_ranges(lst: list):
    if not lst:
        return []
    result = []
    sublists = []
    current_list = [lst[0]]
    for el1, el2 in zip(lst, lst[1:]):
        if el2 - el1 == 1:
            current_list.append(el2)
        else:
            sublists.append(current_list)
            current_list = [el2]
    sublists.append(current_list)

    for sublist in sublists:
        if len(sublist) > 1:
            result.append(f"{sublist[0]}->{sublist[-1]}")
    return result
