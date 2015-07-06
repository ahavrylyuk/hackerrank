#! /usr/bin/env python3


def find_number_of_paths(n, m, obs):
    field = [[0]*m for _ in range(n)]
    for i, j in obs:
        field[i][j] = 1
    cache = [[0]*m for _ in range(n)]
    cache[0][-1] = 1
    for i in range(n):
        for j in range(m):
            if field[i][j] is 1:
                continue
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
    return cache[n - 1][m - 1]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = (int(x) for x in input().split())
        obs = [[int(y) for y in list(x)] for x in input().split()]
        print(find_number_of_paths(n, m, obs))
