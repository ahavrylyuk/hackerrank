#! /usr/bin/env python

n, m = (int(i) for i in input().split())
total = 0
for _ in range(m):
    a, b, k = (int(i) for i in input().split())
    total += (b - a + 1) * k
print(total // n)
