#! /usr/bin/env python


def checkio(data):
    elements = data[:]
    elements.sort()
    length = len(elements)
    if length % 2 == 1:
        return elements[length // 2]
    else:
        return (elements[length // 2 - 1] + elements[length // 2]) / 2


if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3
    assert checkio([3, 1, 2, 5, 3]) == 3
    assert checkio([1, 300, 2, 200, 1]) == 2
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
