#! /usr/bin/env python


def sqr_count(a, b):
    sqrt_a = a ** .5
    start = int(sqrt_a)
    end = int(b ** .5)
    return end - start + (1 if sqrt_a.is_integer() else 0)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(sqr_count(*map(int, input().split())))
