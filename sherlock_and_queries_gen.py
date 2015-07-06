#! /usr/bin/env python
from random import randrange


def random_gen(n):
    for _ in range(n):
        yield randrange(1, n)


if __name__ == '__main__':
    n = 10 ** 4
    print(n, n)
    res = ' '.join(map(str, random_gen(n)))
    print(res)
    print(res)
    print(res)
