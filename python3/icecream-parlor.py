#!/usr/bin/env python3

def solve(m, a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if i != j and a[i] + a[j] == m:
                return [i + 1, j + 1]

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        m = int(input())
        input()
        a = [int(x) for x in input().split()]
        print(' '.join([str(x) for x in solve(m, a)]))
