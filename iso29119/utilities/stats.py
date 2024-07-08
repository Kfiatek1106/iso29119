def ratio(items, total) -> float:
    return items/total


def print_in_percen(items, total, precision: int = 2) -> str:
    if total <= 0:
        total = 1

    value = 100 * ratio(items, total)

    return f'{round(value, precision)} %'
