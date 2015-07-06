#! /usr/bin/env python


def checkio(value):
    symbols = [c.lower() for c in value if c.isalpha()]
    symbols_count = {c: symbols.count(c) for c in symbols}
    max_count = max(symbols_count.values())
    return min([c for c, count in symbols_count.items() if count == max_count])


if __name__ == '__main__':
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo!!!!") == "a"
    assert checkio("abe") == "a"
