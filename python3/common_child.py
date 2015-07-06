#! /usr/bin/env python


def common_sub(a, b):
    prev = [0] * len(b)
    for i, ai in enumerate(a):
        current = [0] * len(b)
        for j, bj in enumerate(b):
            if j > 0:
                current[j] = prev[j - 1] + 1 if ai == bj \
                    else max(current[j - 1], prev[j])
        prev = current

    return prev[len(b) - 1]

if __name__ == '__main__':
    print(common_sub(input(), input()))
