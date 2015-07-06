#! /usr/bin/env python


def last_stones(n, a, b):
    n = n - 1
    a, b = min(a, b), max(a, b)
    step = b - a
    if step == 0:
        return [n * a]
    return [i for i in range(n * a,  n * b + step, step)]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        res = last_stones(*(int(input()) for _ in range(3)))
        print(' '.join(map(str, res)))
