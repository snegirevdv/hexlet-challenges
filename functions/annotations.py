from functools import wraps


def format_error(error):
    """Format type violation message."""
    argument, value, expected_type = error
    return (
        f'Bad argument type for argument "{argument}":'
        f' {type(value)} instead of {expected_type}'
    )


def throw_errors(info):
    """Raise one error for all typing violations."""
    if isinstance(info, list):
        raise TypeError('\n'.join(map(format_error, info)))
    raise TypeError(format_error(info))


def typechecker(error_callback, stop_after_error):
    def wrapper(func):
        @wraps(func)
        def inner(**kwargs):
            annotations = func.__annotations__
            errors = []
            for argument in kwargs:
                value = kwargs[argument]
                expected_type = annotations[argument]
                if (
                    argument in annotations and
                    not isinstance(value, expected_type)
                ):
                    errors.append((argument, value, expected_type))
                    if stop_after_error:
                        return error_callback(*errors[0])
            return func(**kwargs) if not errors else error_callback(errors)
        return inner
    return wrapper


def typecheck(error_callback=throw_errors):
    return typechecker(error_callback, stop_after_error=True)


def typecheck_all(error_callback=throw_errors):
    return typechecker(error_callback, stop_after_error=False)


if __name__ == '__main__':
    @typecheck_all()
    def multiply(times: int, value: (str, tuple)):
        return value * times

    print(multiply(times=10, value=(42,)))
    print(multiply(times=10, value='1'))

    print(multiply(times='12', value=None))
