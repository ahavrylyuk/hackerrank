#! /usr/bin/env python

from fractions import gcd


def gcd_of_array(n, s):
    if n is 1:
        return s[0]
    return gcd(s[0], gcd_of_array(n - 1, s[1:]))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        value = [int(x) for x in input().split()]
        print('YES' if gcd_of_array(n, value) is 1 else 'NO')
