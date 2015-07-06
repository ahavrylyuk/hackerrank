#! /usr/bin/env python3

# 1 2 3 4 5
from pprint import pprint


def non_palindrom(n, m):
    cache = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            cache[i][j] += cache[i][j - 1] + cache[i - 1][j]
            if i is 0 or j is 0:
                cache[i][j] += 1
    pprint(cache)
    return 0


if __name__ == '__main__':
    t = int(input())
    modulo = 10 ** 9 + 7
    for _ in range(t):
        print(non_palindrom(*(int(x) for x in input().split())) % modulo)
