#! /usr/bin/env python


def max_subsum(n, a):
    positive_sum, current_sum, best_sum = (0,) * 3
    has_positive = False
    max_negative = a[0]
    for i in range(n):
        if a[i] > 0:
            has_positive = True
            positive_sum += a[i]
        elif a[i] > max_negative:
            max_negative = a[i]

        val = current_sum + a[i]
        if val > 0:
            current_sum = val
        else:
            current_sum = 0
        if current_sum > best_sum:
            best_sum = current_sum
    if has_positive:
        return (best_sum, positive_sum)
    else:
        return (max_negative, max_negative)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(int(x) for x in input().split())
        res = max_subsum(n, a)
        print(' '.join(map(str, res)))
