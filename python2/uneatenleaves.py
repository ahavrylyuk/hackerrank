#!/usr/bin/env python


def countUneatenLeaves(N, A):
    eaten = set()
    for a in A:
        eaten = eaten.union(xrange(a, N, a))
    return N - 1 - len(eaten)


print countUneatenLeaves(10, [2, 4, 5])
