#! /usr/bin/env python


def gifts(b, w, x, y, z):
    b_cost = x if y + z > x else y + z
    w_cost = y if x + z > y else x + z
    return b * b_cost + w * w_cost


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        b, w = [int(x) for x in input().split()]
        x, y, z = [int(x) for x in input().split()]
        print(gifts(b, w, x, y, z))
