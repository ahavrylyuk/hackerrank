#! /usr/bin/env python


def is_pal(s):
    return s == s[::-1]


def p_index(s):
    i, j = 0, len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    if i == j:
        return -1
    if is_pal(s[i + 1: j + 1]):
        return i
    if is_pal(s[i: j]):
        return j


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(p_index(input()))
