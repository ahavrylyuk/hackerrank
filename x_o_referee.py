#! /usr/bin/env python


def checkio(value):
    length = len(value)
    binary = lambda v: [[1 if x == v else 0 for x in line] for line in value]

    xs, os = binary('X'), binary('O')

    sum_diag = lambda m: sum([m[i][i] for i in range(len(m))])
    sum_rdiag = lambda m: sum([m[i][length - 1 - i] for i in range(len(m))])
    sum_line = lambda m: sum([_ for _ in m[i]])
    sum_row = lambda m: sum([_[i] for _ in m])

    if sum_diag(xs) == length or sum_rdiag(xs) == length:
        return 'X'
    if sum_diag(os) == length or sum_rdiag(os) == length:
        return 'O'

    for i in range(length):
        if (sum_line(xs) == length or sum_row(xs) == length):
            return 'X'
        if (sum_line(os) == length or sum_row(os) == length):
            return 'O'
    return 'D'


if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", '#1'
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", '#2'
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", '#3'
    assert checkio([
        "OOO",
        "XXO",
        "OXX"]) == "O", '#4'
    assert checkio([
        "OXX",
        "XOX",
        "XXO"]) == 'O', '#5'
    assert checkio([
        "XXO",
        "XOX",
        "OXX"]) == 'O', '#6'
