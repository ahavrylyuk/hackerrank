#! /usr/bin/env python


def change(n, m, A, B, C, mod):
    mulx = {}
    for i in range(m):
        b = mulx.get(B[i], 1)
        mulx[B[i]] = b * C[i] % mod
    for i, mul in mulx.items():
        for j in range(i - 1, n, i):
            A[j] = A[j] * mul % mod


if __name__ == '__main__':
    read = lambda: map(int, input().split())
    (n, m), a, b, c = (list(read()) for _ in range(4))
    change(n, m, a, b, c, 10 ** 9 + 7)
    print(' '.join(map(str, a)))
