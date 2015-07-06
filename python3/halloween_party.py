#! /usr/bin/env python


def max_pieces(k):
    horizontal = int(k / 2)
    vertical = k - horizontal
    return horizontal * vertical


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(max_pieces(int(input())))
