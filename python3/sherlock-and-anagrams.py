#!/usr/bin/env python3

from collections import defaultdict
from collections import Counter


def count_anagrams(s):
    len_s = len(s)
    substrs = defaultdict(list)
    count = 0
    for length in range(1, len_s):
        same_len = substrs[length]
        for i in range(len_s - length + 1):
            substr = Counter(s[i:i + length])
            count += sum(1 for _ in same_len if _ == substr)
            same_len.append(substr)
    return count


t = int(input())
for _ in range(t):
    print(count_anagrams(input()))
