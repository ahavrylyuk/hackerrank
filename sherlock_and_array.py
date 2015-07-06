#! /usr/bin/env python


def is_simetric_sum(n, a):
    left, right = 0, sum(a) - a[0]
    for i in range(n - 1):
        if left == right:
            return True
        left += a[i]
        right -= a[i + 1]
    return n == 1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print('YES' if is_simetric_sum(n, a) else 'NO')
