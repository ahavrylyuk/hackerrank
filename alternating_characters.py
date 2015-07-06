#! /usr/bin/env python


def alter_min(s):
    c, res = s[0], 0
    for i in range(1, len(s)):
        if s[i] == c:
            res += 1
        else:
            c = s[i]
    return res


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(alter_min(input()))
