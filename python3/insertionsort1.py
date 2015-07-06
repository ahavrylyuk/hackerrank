#! /usr/bin/env python


def sort_steps(n, a):
    el = a[-1]
    for i in range(n - 2, -2, -1):
        if i is -1 or a[i] <= el:
            a[i + 1] = el
            yield a
            break
        a[i + 1] = a[i]
        yield a


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    res = sort_steps(n, a)
    for _ in res:
        print(' '.join(map(str, _)))
