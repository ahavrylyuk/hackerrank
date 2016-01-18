#!/usr/bin/env python


def countUneatenLeaves(N, A):
    jumps = set()
    for a in sorted(A):
        if any([not a % j for j in jumps]):
            continue
        jumps.add(a)
    eaten = sum([len(xrange(j, N, j)) for j in jumps])
    return N - 1 - eaten


print countUneatenLeaves(10, [2, 4, 5])
