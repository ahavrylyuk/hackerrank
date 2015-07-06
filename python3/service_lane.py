#! /usr/bin/env python


def largets_vehicle(n, width, i, j):
    vehicle = 3
    for k in range(i, j + 1):
        if width[k] < vehicle:
            vehicle = width[k]
    return vehicle


if __name__ == '__main__':
    read_n = lambda: list(map(int, input().split()))
    n, t = read_n()
    width = read_n()
    for _ in range(t):
        print(largets_vehicle(n, width, *read_n()))
