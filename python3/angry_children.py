#! /usr/bin/env python


def min_u(n, k, *args):
    values = list(args)
    values.sort()
    min_diff = None
    for i in range(n - k + 1):
        diff = values[i + k - 1] - values[i]
        if (min_diff is None or min_diff > diff):
            min_diff = diff
    return min_diff


if __name__ == '__main__':
    n = int(input())
    print(min_u(n, *[int(input()) for _ in range(n + 1)]))
