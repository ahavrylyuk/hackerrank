#! /usr/bin/env python

from collections import defaultdict


def dfs_visit(parent, g, start):
    for v in g[start]:
        counts[start].add(v)
        if v not in parent:
            parent.append(v)
            subtree = dfs_visit(parent, g, v)
            for u in subtree:
                if u != start:
                    counts[start].add(u)
    return counts[start]


def read_line():
    return (int(x) for x in input().split())

if __name__ == '__main__':
    g = defaultdict(set)
    n, m = read_line()
    for _ in range(m):
        vi, ui = read_line()
        g[vi].add(ui)
        g[ui].add(vi)
    start = next(iter(g))
    parent = [start]
    counts = defaultdict(set)
    dfs_visit(parent, g, start)
    from pprint import pprint
    pprint(counts)
    print(sum(1 for x in counts.values() if len(x) % 2 is 0))
