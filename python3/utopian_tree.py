#! /usr/bin/env python


def height(cycles):
    res = 1
    for i in range(cycles):
        delta = 1 if i % 2 else res
        res += delta
    return res


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = input()
        res = height(int(a))
        print(res)
