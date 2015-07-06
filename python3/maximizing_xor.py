#! /usr/bin/env python


def xor(l, r):
    xors, values = [], list(range(l, r + 1))
    for a in values:
        for b in values:
            xors.append(a ^ b)
    return max(xors)


if __name__ == '__main__':
    print(xor(*(int(input()) for _ in range(2))))
