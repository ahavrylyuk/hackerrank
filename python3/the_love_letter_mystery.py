#! /usr/bin/env python


def palin_min(s):
    res, len_s = 0, len(s)
    for i in range(len_s // 2):
        left, right = ord(s[i]), ord(s[len_s - 1 - i])
        res += abs(left - right)
    return res


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(palin_min(input()))
