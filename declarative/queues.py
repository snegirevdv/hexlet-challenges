from collections.abc import Iterator


def round_robin2(*iterables) -> Iterator:
    iters = [iter(iterable) for iterable in iterables]
    needs_break = False
    while not needs_break:
        needs_break = True
        indexes_to_pop = []
        for index, iterator in enumerate(iters):
            try:
                yield next(iterator)
                needs_break = False
            except StopIteration:
                indexes_to_pop.append(index)
        for delta, index in enumerate(indexes_to_pop):
            iters.pop(index - delta)
