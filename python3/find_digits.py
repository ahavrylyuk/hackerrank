#! /usr/bin/env python


def digits(n):
    ds = list(map(int, str(n)))
    count = 0
    for d in ds:
        if d > 0 and n % d == 0:
            count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(digits(int(input())))
