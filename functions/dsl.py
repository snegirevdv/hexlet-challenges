from collections import deque
from collections.abc import Callable
from functools import wraps


def simple_input(_, prompt):
    return input(prompt)


def asks(name: str, prompt: str) -> Callable:
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs) -> Callable:
            return func(*args, **kwargs)

        if not hasattr(inner, "wrapped_args"):
            inner.wrapped_args = deque()
        inner.wrapped_args.appendleft((name, prompt))

        return inner

    return wrapper


def interactive(
    description: str,
    input_function: Callable = simple_input,
    output_function: Callable = print,
) -> Callable:
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs) -> None:
            output_function(description)

            if hasattr(func, "wrapped_args"):
                kwargs.update(
                    {
                        name: input_function(name, prompt)
                        for name, prompt
                        in func.wrapped_args
                    }
                )

            output_function(func(*args, **kwargs))

        return inner

    return wrapper


@interactive('Calculator')
@asks('x', 'Enter first number: ')
@asks('y', 'Enter second number: ')
def calc(x: str, y: str) -> int:
    return int(x) + int(y)


if __name__ == '__main__':
    calc()
