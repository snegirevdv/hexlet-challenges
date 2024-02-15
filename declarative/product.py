# https://ru.hexlet.io/challenges/python_declarative_programming_cartesian_product_exercise

def product(head, *tail) -> list[tuple]:
    tail_product = product(*tail) if tail else ['']
    return [
        (head_element, *tail_element)
        for head_element in head
        for tail_element in tail_product
    ]
