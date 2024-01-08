# https://ru.hexlet.io/courses/python-functions/lessons/positional-args/theory_unit

from collections.abc import Callable
from functools import wraps


def format_error(error):
    """Format type violation message."""
    argument, value, expected_type = error
    return (
        f'Bad argument type for argument "{argument}":'
        f' {type(value)} instead of {expected_type}'
    )


def throw_error(*args):
    """Raise one typing violation."""
    raise TypeError(format_error(args))


def throw_errors(errors):
    """Raise one error for all typing violations."""
    raise TypeError('\n'.join(map(format_error, errors)))


def check_errors_and_raise(kwargs: dict,
                           annotations: dict,
                           error_response: Callable,
                           stop_after_error: bool,
                           ) -> bool:
    has_errors = False
    for argument in kwargs:
        value = kwargs[argument]
        expected_type = annotations[argument]
        try:
            if (
                argument in annotations and
                not isinstance(value, expected_type)
            ):
                raise TypeError
        except TypeError:
            error_response(argument, value, expected_type)
            has_errors = True
            if stop_after_error:
                return has_errors
    return has_errors


def typecheck(error_callback=throw_error):
    """
    Добавляет к функции предусловие, проверяющие типы аргументов.

    Проверка типов делается на основе аннотаций, указанных в сигнатуре
    оборачиваемой функции.

    Arguments:
        error_callback - функция, получающая информацию об ошибке типизации.
        Функция принимает имя аргумента, значение и ожидаемый тип.
        Обычно error_callback ничего не возвращает, а вместо этого возбуждает
        исключение (см. реализацию по умолчанию - throw_error).

    Returns:
        Декоратор, добавляющий проверку типов к функции.

    """
    def wrapper(func):
        @wraps(func)
        def inner(**kwargs):
            annotations = func.__annotations__
            has_errors = check_errors_and_raise(
                kwargs,
                annotations,
                error_response=error_callback,
                stop_after_error=True,
            )
            if not has_errors:
                return func(**kwargs)
        return inner
    return wrapper


def typecheck_all(error_callback=throw_errors):
    """
    Добавляет к функции предусловие, проверяющие типы аргументов.

    Проверка типов делается на основе аннотаций, указанных в сигнатуре
    оборачиваемой функции.

    Arguments:
        error_callback - функция, получающая информацию об ошибке типизации.
        Функция принимает список кортежей, описывающих все ошибки типизации.
        Каждый кортеж содержит имя аргумента, значение и ожидаемый тип.
        Обычно error_callback ничего не возвращает, а вместо этого возбуждает
        исключение (см. реализацию по умолчанию - throw_errors).

    Returns:
        Декоратор, добавляющий проверку типов к функции.

    """
    def wrapper(func):
        @wraps(func)
        def inner(**kwargs):
            errors = []
            annotations = func.__annotations__
            has_errors = check_errors_and_raise(
                kwargs,
                annotations,
                error_response=lambda *x: errors.append((x)),
                stop_after_error=False,
            )
            print(errors)
            if not has_errors:
                return func(**kwargs)
            error_callback(errors)
        return inner
    return wrapper


if __name__ == '__main__':
    @typecheck_all()
    def multiply(times: int, value: (str, tuple)):
        return value * times

    print(multiply(times=10, value=(42,)))
    print(multiply(times=10, value='1'))

    # оба аргумента — не того типа
    print(multiply(times='12', value=None))
