#!/usr/bin/env python


def gcd(*numbers):
    from fractions import gcd
    return reduce(gcd, numbers)


def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)


def countUneatenLeaves(N, A):
    alone = [N//a for a in A]
    together = N//lcm(*A)
    pairs = [0]*len(A)
    for i in range(-1, len(A) - 1):
        pairs[i + 1] = N//lcm(A[i], A[i + 1])
    return N - (sum(alone) + together - sum(pairs))


print countUneatenLeaves(10, [2, 5, 4])
