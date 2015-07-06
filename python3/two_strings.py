#! /usr/bin/env python


def has_common(a, b):
    return len(set(a) & set(b)) > 0


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = (input() for _ in range(2))
        print('YES' if has_common(a, b) else 'NO')
