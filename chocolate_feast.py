#! /usr/bin/env python

# 3
# 10 2 5
# 12 4 4
# 6 2 2


def divide(a, b):
    return (a // b, a % b)


def chocolates(n, c, m):
    count, _ = divide(n, c)
    free = count
    while free >= m:
        free, rest = divide(free, m)
        count += free
        free += rest
    return count


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(chocolates(*[int(x) for x in input().split()]))
