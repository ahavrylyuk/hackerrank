#! /usr/bin/env python


def count_routes(n, a):
    count = 1
    for i in range(len(a)):
        count *= a[i]
    return count


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print(count_routes(n, a) % 1234567)
