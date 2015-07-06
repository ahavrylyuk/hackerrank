#!/usr/bin/env python3


def max_sqr(l, b):
    side = min(l, b)
    sqr = l * b
    max_side = (0, 0)
    for i in range(1, side + 1):
        if l % i is 0 and b % i is 0:
            squares = sqr/(i*i)
            if squares.is_integer() and i > max_side[0]:
                max_side = (i, squares)
    return int(max_side[1])


t = int(input())
for _ in range(t):
    print(max_sqr(*[int(x) for x in input().split()]))
