#! /usr/bin/env python


def cut_the_sticks(a):
    cuts = []
    while len(a) > 0:
        cutter = a.pop()
        if cutter == 0:
            continue
        for i in range(len(a)):
            a[i] -= cutter
        cuts.append(len(a) + 1)
    return cuts

if __name__ == '__main__':
    _ = input()
    value = map(int, input().split(' '))
    res = cut_the_sticks(sorted(value, reverse=True))
    for v in res:
        print(v)
