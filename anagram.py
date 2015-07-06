#! /usr/bin/env python

from collections import Counter


def anagram_replace_count(s):
    len_s = len(s)

    if len_s % 2 is not 0:
        return -1

    s1 = Counter(s[:len_s//2])
    s2 = Counter(s[len_s//2:])

    negative = positive = 0

    for l, count in s1.items():
        diff = s2.get(l, 0) - count
        if diff > 0:
            positive += diff
        if diff < 0:
            negative += diff

    return max(map(abs, (positive, negative)))

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(anagram_replace_count(input()))
