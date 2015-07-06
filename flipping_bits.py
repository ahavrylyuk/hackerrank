#! /usr/bin/env python


def binary(value):
    """ return array of 32 binary bits """
    res = []
    while value > 0:
        res.append(value % 2)
        value = value // 2
    return [0] * (32 - len(res)) + res[::-1]


def flip_elements(iterable):
    return [1 if e == 0 else 0 for e in iterable]


def decimal(binary):
    res = 0
    for i, v in enumerate(reversed(binary)):
        if v:
            res += pow(2, i)
    return res


def flip(a):
    return decimal(flip_elements(binary(a)))


def flip_native(a):
    return a ^ (2 ** 32 - 1)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = input()
        res = flip(int(a))
        print(res)
