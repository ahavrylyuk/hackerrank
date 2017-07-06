#!/usr/bin/env python


def countUneatenLeaves(N, A):
    leaves = [0]*N
    for i in xrange(1, N):
        for a in A:
            if i % a is 0:
                leaves[i] = 1
    return N - 1 - sum(leaves)

print countUneatenLeaves(10**8, [2, 4, 5])
