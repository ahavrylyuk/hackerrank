#!/usr/bin/env python3

s1 = input()
s2 = input()

letters = [[0]*2 for _ in range(26)]
start = ord('a')
for c1 in map(ord, s1):
    letters[c1 - start][0] += 1
for c2 in map(ord, s2):
    letters[c2 - start][1] += 1
count = 0
for c1, c2 in letters:
    count += abs(c1 - c2)

print(count)
