#! /usr/bin/env python


def decent(n):
    count5, count3 = n // 3, 0
    is_decent = lambda: 3 * count5 + 5 * count3 == n
    while count5 > 0 and count3 <= n // 5:
        if is_decent():
            break
        count3 += 1
        count5 = (n - 5 * count3) // 3
    if is_decent():
        return '555' * count5 + '33333' * count3
    return -1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(decent(int(input())))
