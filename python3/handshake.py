#! /usr/bin/env python


def handshake(n):
    return n * (n - 1) // 2


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(handshake(n))
