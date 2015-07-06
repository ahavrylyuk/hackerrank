#! /usr/bin/env python
import random

if __name__ == '__main__':
    n = 500
    print(n, n)
    for i in range(n):
        values = [str(random.randrange(100, 1000) % 2) for _ in range(n)]
        print(''.join(values))
