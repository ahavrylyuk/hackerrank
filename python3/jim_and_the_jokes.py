#! /usr/bin/env python

from collections import defaultdict
from contextlib import suppress

if __name__ == '__main__':
    t = int(input())
    dates = defaultdict(int)
    for _ in range(t):
        base, value = input().split()
        with suppress(ValueError):
            dates[int(value, int(base))] += 1
    print(sum(c*(c - 1)//2 for c in dates.values()))
