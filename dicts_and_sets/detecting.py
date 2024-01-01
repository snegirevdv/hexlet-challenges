# https://ru.hexlet.io/challenges/python_dicts_find_where_exercise


def is_match(book: dict, request: dict) -> bool:
    try:
        return all(book[param] == request[param] for param in request)
    except KeyError:
        return False


def find_where(books: list[dict], request: dict) -> dict | None:
    for book in books:
        if is_match(book, request):
            return book
    return None
