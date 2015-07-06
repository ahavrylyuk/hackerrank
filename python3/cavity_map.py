#! /usr/bin/env python

cavity_flag = 10

indexes = (-1, 0), (1, 0), (0, -1), (0, 1)


def cavity(val):
    end = len(val) - 1
    for i in range(1, end):
        for j in range(1, end):
            values = [val[i + _[0]][j + _[1]] for _ in iter(indexes)]
            if max(values) < val[i][j]:
                val[i][j] = cavity_flag

if __name__ == '__main__':
    n = int(input())
    value = list(list(int(v) for v in x) for x in [input() for _ in range(n)])
    cavity(value)
    for v in value:
        print(''.join(str(x) if x < cavity_flag else 'X' for x in v))
