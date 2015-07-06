#! /usr/bin/env python


def is_cancelled(n, k, a):
    return sum(1 for x in a if x <= 0) < k

if __name__ == '__main__':
    t = int(input())
    read = lambda: (int(x) for x in input().split())
    for _ in range(t):
        (n, k), a = read(), read()
        print('YES' if is_cancelled(n, k, a) else 'NO')
