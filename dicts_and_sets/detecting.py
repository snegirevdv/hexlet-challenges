# https://ru.hexlet.io/challenges/python_dicts_find_where_exercise

# Реализуйте функцию find_where(). Она должна принимать на вход список книг
# и поисковый запрос, а затем возвращать первую книгу, которая соответствует
# запросу.

# Решение
def is_match(book: dict, request: dict) -> bool:
    for param, value in request.items():
        # if book.get(param, object()) != value:
        if param not in book or book[param] != value:
            return False
    return True


def find_where(books: list[dict], request: dict) -> dict | None:
    for book in books:
        if is_match(book, request):
            return book
    return None


# Тесты
TITLE, AUTHOR, YEAR = 'title', 'author', 'year'
BOOKS = [
    {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111},
    {TITLE: 'Cymbeline', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'The Tempest', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'Book of Foos Barrrs', AUTHOR: 'FooBar', YEAR: 2222},
    {TITLE: 'Still foooing', AUTHOR: 'FooBar', YEAR: 333},
    {TITLE: 'Happy Foo', AUTHOR: 'FooBar', YEAR: 4444},
]


def test_find_where():
    assert find_where(BOOKS, {}) == BOOKS[0]

    assert find_where(BOOKS, {AUTHOR: 'Pushkin'}) is None

    assert find_where(BOOKS, {YEAR: 1111, AUTHOR: 'Pushkin'}) is None

    assert find_where(BOOKS, {"genre": None}) is None

    assert find_where(
        BOOKS, {YEAR: 1111},
    ) == {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111}

    assert find_where(
        BOOKS, {AUTHOR: 'Shakespeare', YEAR: 1611},
    )[TITLE] == 'Cymbeline'

    assert find_where(BOOKS, BOOKS[2]) == BOOKS[2]


test_find_where()
