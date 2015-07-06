#! /usr/bin/env python

fibo = set()
current, prev = 1, 1
last = 10 ** 10
while current < last:
    fibo.add(current)
    current, prev = current + prev, current


def is_fibo(n):
    return n in fibo


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print('IsFibo' if is_fibo(int(input())) else 'IsNotFibo')
